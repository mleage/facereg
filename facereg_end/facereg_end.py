# -*- coding: utf-8 -*-
import cv2

import math

import PyQt5

from PyQt5 import QtCore, QtGui, QtWidgets,QtMultimedia

from PyQt5.QtWidgets import *

from PyQt5.QtCore import *

from PyQt5.QtGui import *

import os

import sys

from OtherWidget import *
from Mythread import *
from UI import *





#继承终端UI实现相关逻辑 
class end(end_UI):
    def __init__(self,parent = None):
        super(end,self).__init__(parent)
        self.initLogic()
        
    #初始化逻辑
    def initLogic(self):
        self.initCamera()
        self.initTime()
        self.read_local_device_info()
        self.set_upload_device_timer()
        
        #点击后开启获取数据库的线程
        self.right_widget.ok.clicked.connect(self.getOP)
    
    #添加键盘相应事件,按下enter,相当于点击确认按钮
    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Enter:
            self.getOP()

    #初始化显示时间
    def initTime(self):
        self.timer_Time = QTimer()
        self.timer_Time.setInterval(1000 * 1)#一秒钟
        self.timer_Time.start()
        self.timer_Time.timeout.connect(self.show_time)
    
    #获取当前时间并显示到相应标签
    def show_time(self):
        # 格式化成2016-03-20 11:45:39形式
        cur_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) 
        self.lable_time.setText(cur_time)    
    
    #创建新线程获取数据库信息
    def getOP(self):
        #判断是否有输入,没有输入直接退出
        if self.right_widget.get_id.text() == '':
            return
        #获取输入的账号信息
        self.id = self.right_widget.get_id.text()

        #实例化线程并运行
        self.thread_getOP = DatabaseThread(self.id)
        #信息获取成功后判断是否有效并进行人脸核验
        self.thread_getOP.signal.connect(self.judge_pass)
        self.thread_getOP.start()

    #判断输入是否正确,然后进行人脸核验,res为获取数据库信息线程发送的信息
    def judge_pass(self,res):
        if res == None:
            #没有该用户，进行语音播报并退出
            self.thread1 = AudioThread(1)
            self.thread1.start()
            self.show_user_not_exist()
            return 
       
        #暂存现在的学生基础信息
        self.cur_stu_info = trans_to_studentinfo(res)

        #判断该学生是否已经核验过了
        if self.cur_stu_info.isreg == 1:
            #播报相关语音
            self.thread4 = AudioThread(4)
            self.thread4.start()
            self.show_user_repeat()
            return 

        #接下来进行人脸核验
        #直接开辟线程获取识别结果,识别结果获取后通知相关函数,进行后续处理
        self.thread_getReg = RegThread('Capture1.png',res[1])
        self.thread_getReg.signal.connect(self.show_result)
        self.thread_getReg.start()


    #显示人脸验证结果,res为获取识别概率的线程发送的信息
    def show_result(self,res):
        self.confidence1 = res
        #判断是否能识别
        if self.confidence1 == None:
            self.confidence1 = 0

        #maxconf 表示两个摄像头获取的图像分别进行识别后返回的最大值
        maxconf = self.confidence1
        if maxconf > 75:
            #语音播报线程
            self.thread2 = AudioThread(2)
            self.thread2.start()

            #上传核验成功信息,开启新的线程
            self.thread_upload = UploadThread(1,self.cur_stu_info,self.confidence1)
            self.thread_upload.start()

            #显示核验成功信息
            self.show_done_info()
        else:
            #播放音频线程
            self.thread3 = AudioThread(3)
            self.thread3.start()

            #上传核验失败信息，开启新的线程
            self.thread_upload = UploadThread(0,self.cur_stu_info,self.confidence1)
            self.thread_upload.start()

            #显示核验失败信息
            self.show_false_info()
        
        #显示一会信息，然后初始化界面
        self.stop_and_show()

    #显示一会信息，然后初始化界面
    def stop_and_show(self):
        self.right_widget.get_id.clear()
        self.timer_show = QTimer()
        self.timer_show.setInterval(1000 * 2)#两秒钟
        self.timer_show.timeout.connect(self.clear_all)
        self.timer_show.start()

    #显示用户核验成功的信息
    def show_done_info(self):
        self.right_widget.save_pic.setPixmap(QPixmap(self.cur_stu_info.picture).scaled(200,200))
        self.right_widget.save_pic2.setPixmap(QPixmap('Capture3.png').scaled(200,200))
        self.right_widget.label_hint.setText('人脸核验成功!')
        self.right_widget.lable_name.setText(self.cur_stu_info.name)
        self.right_widget.lable_id.setText(self.cur_stu_info.regId)

    #显示用户核验失败信息
    def show_false_info(self):
        self.right_widget.label_hint.setText('人脸核验失败!')
    
    #显示用户不存在信息
    def show_user_not_exist(self):
        self.right_widget.label_hint.setText('用户不存在!')
        self.right_widget.get_id.clear()
        self.stop_and_show()

    #用户重复核验
    def show_user_repeat(self):
        self.right_widget.label_hint.setText('你已核验成功,请勿重试!')
        self.right_widget.get_id.clear()
        self.stop_and_show()    
    #初始化所有的标签显示
    def clear_all(self):
        self.right_widget.label_hint.setText('人脸识别中...')
        self.right_widget.lable_name.setText('姓名')
        self.right_widget.lable_id.setText('学生号')
        self.right_widget.save_pic.setPixmap(self.right_widget.pixmap)
        self.right_widget.save_pic2.setPixmap(self.right_widget.pixmap2)

    #初始化相机
    def initCamera(self):
        self.timer_camera = QTimer()
        self.timer_camera.setInterval(30)#30ms 更新一次
        self.timer_camera.start()
        self.timer_camera.timeout.connect(self.show_camera)
        self.face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        self.face_cascade.load('haarcascade_frontalface_default.xml')
        self.CAM_num1 = 0
        self.CAM_num2 = 0
        self.capture1 = cv2.VideoCapture(self.CAM_num1)
        self.capture2 = cv2.VideoCapture(self.CAM_num2)

    #关闭程序时,清除相应的资源
    def closeEvent(self,event):
        self.timer_camera.stop()
        self.timer_Time.stop()
        self.capture1.release()
        self.capture2.release()
        # cv2.destroyAllWindows()
        event.accept()

    #显示第一个摄像头画面
    def show_camera1(self):
        flag1, self.image1 = self.capture1.read()
        #获取捕获的图片
        cv2.imwrite("Capture1.png",self.image1)
        show_image1 = cv2.resize(self.image1, (640, 480))
        # 将读取的图像转为COLOR_BGR2GRAY，减少计算强度
        gray1 = cv2.cvtColor(show_image1, cv2.COLOR_BGR2GRAY)
        # 检测出的人脸个数
        faces1 = self.face_cascade.detectMultiScale(gray1, scaleFactor = 1.15, minNeighbors = 5, minSize = (5, 5))
        if len(faces1) == 1:
            # 用矩形圈出人脸的位置
            for(x, y, w, h) in faces1:
                cv2.rectangle(show_image1, (x, y), (x + w, y + h),  (230,70,150), 2)
                mini_image = self.image1[y:y+h,x:x+w]
                cv2.imwrite("Capture3.png",mini_image)

        show_image1 = cv2.cvtColor(show_image1, cv2.COLOR_BGR2RGB)
        #将捕获的图像保存到本地
        cv2.imwrite("Capture5.png",show_image1)
        showImage1 = QtGui.QImage(show_image1.data, show_image1.shape[1], show_image1.shape[0], QtGui.QImage.Format_RGB888)
        self.lable_up_pic.setPixmap(QtGui.QPixmap.fromImage(showImage1))
   
    #显示第二个摄像头画面
    def show_camera2(self):
        flag2, self.image2 = self.capture1.read()

        #获取捕获的图片
        cv2.imwrite("Capture2.png",self.image2)
        show_image2 = cv2.resize(self.image2, (640, 480))

        # 将读取的图像转为COLOR_BGR2GRAY，减少计算强度
        gray2 = cv2.cvtColor(show_image2, cv2.COLOR_BGR2GRAY)
        # 检测出的人脸个数
        faces2 = self.face_cascade.detectMultiScale(gray2, scaleFactor = 1.15, minNeighbors = 5, minSize = (5, 5))
        if len(faces2) == 1:
            # 用矩形圈出人脸的位置
            for(x, y, w, h) in faces2:
                cv2.rectangle(show_image2, (x, y), (x + w, y + h),  (230,70,150), 2)
                mini_image = self.image2[y:y+h,x:x+w]
                cv2.imwrite("Capture4.png",mini_image)
  
        show_image2 = cv2.cvtColor(show_image2, cv2.COLOR_BGR2RGB)
        #将捕获的图像保存到本地
        cv2.imwrite("Capture6.png",show_image2)
        showImage2 = QImage(show_image2.data, show_image2.shape[1], show_image2.shape[0], QtGui.QImage.Format_RGB888)
        self.lable_down_pic.setPixmap(QtGui.QPixmap.fromImage(showImage2))
    
    #显示实时获取的图像，0.3秒刷新一次；保存获取的图像到'Capture1.png'和'Capture2.png'
    def show_camera(self):
        self.show_camera1()
        self.show_camera2()
    
    #设置设备上传的时钟
    def set_upload_device_timer(self):
        self.device_timer = QTimer()
        #设置间隔为100秒
        self.device_timer.setInterval(1000 * 100)
        self.device_timer.timeout.connect(self.upload_devices_info)
        self.device_timer.start()

    #读取本地设备文件
    def read_local_device_info(self):
        fp = open('device.txt')
        content = fp.read()
        content = str.split(content,',')
        self.keyid = content[0]
        self.equipcodeid = content[1]
        print(self.keyid)
        print(self.equipcodeid)
        fp.close()

    #上传设备信息,设备信息进行状态上传,开启新的线程进行
    def upload_devices_info(self):
        self.thread_upload_device = UploadDeviceThread(self.keyid,self.equipcodeid)
        self.thread_upload_device.start()

    #TODO:将捕获的图片交给人脸识别模块进行同步处理，返回相应结果并在界面中做相应提示,实现
    #TODO:将用户的识别信息提交到数据库，包括识别成功与识别失败,实现
    #TODO:行为信息的日志上传,基本实现
    #TODO:程序执行过程中可能出现的异常进行日志上传,未发现异常
    #TODO:定时上传设备状态信息,由于数据表的原因,完成

#将数据库中获取的学生信息转换为实体类，方便修改与使用
def trans_to_studentinfo(tuple_stu):
    print(len(tuple_stu))
    print(tuple_stu[0])
    stu = StudentInfo.Student(tuple_stu[0],tuple_stu[1],tuple_stu[2],tuple_stu[3],tuple_stu[4],\
        tuple_stu[5],tuple_stu[7],tuple_stu[9],tuple_stu[10],tuple_stu[11],tuple_stu[12],\
            tuple_stu[13],tuple_stu[14],tuple_stu[16],tuple_stu[17],tuple_stu[18])
    return stu


def main():
    app = QApplication(sys.argv)
    Ex = end() 
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
    # db = stuDAO.stuDAO()
    # db.writeStudentIntoExecl()
    # read_local_device_info()