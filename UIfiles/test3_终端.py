# -*- coding: utf-8 -*-
import cv2

from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtWidgets import *

from PyQt5.QtCore import *

from PyQt5.QtGui import *

import os
import time

import sys
from DATABASEOP import *
from DATABASEOP import *



class Right_widget(QWidget):
    def __init__(self,parent = None):
        super(Right_widget,self).__init__(parent)
        self.initUI()

    #画图时间
    def paintEvent(self,event):

        qp = QPainter()
        qp.begin(self)
        self.drawLines(qp)
        qp.end()
 
    #在界面上画出下划线
    def drawLines(self, qp):
        pen = QPen(Qt.black, 2, Qt.SolidLine)
        pen.setColor(Qt.white)
        qp.setPen(pen)
        qp.drawLine(50, 500, 500, 500)
 
        # pen.setStyle(Qt.DashLine)
        qp.setPen(pen)
        qp.drawLine(50, 670, 500, 670)

    def initUI(self):
        self.setStyleSheet('''font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
        font-size:30px;color:white;''')
        self.save_pic = QLabel(self)
        self.save_pic.setStyleSheet('background:rgb(30,30,30);')


        self.save_pic.setFixedSize(200,200)

        self.pixmap = QPixmap('./Icon/default_head.png')
        self.pixmap  = self.pixmap.scaled(200,200)

        self.save_pic.setPixmap(self.pixmap)
        self.layout_save_pic = QHBoxLayout()
        self.layout_save_pic.addWidget(self.save_pic)
        self.temp = QWidget()
        self.temp.setLayout(self.layout_save_pic)

        self.right_layout = QVBoxLayout()
        self.right_layout.setSpacing(10)
        self.label_hint = QLabel('人脸识别中...',self)
        self.label_hint.setAlignment(Qt.AlignCenter)
        self.lable_id = QLabel('学号',self)
        self.lable_id.setAlignment(Qt.AlignCenter)
        self.lable_name = QLabel('姓名',self)
        self.lable_name.setAlignment(Qt.AlignCenter)

        self.get_id = QLineEdit(self)
        self.get_id.setFixedSize(400,40)
        self.get_id.setPlaceholderText('请输入身份证号')
        self.get_id.setMaxLength(18)
        self.ok = QPushButton("确定",self)

        self.down_layout = QHBoxLayout()
        self.down_layout.addWidget(self.get_id)
        self.down_layout.addWidget(self.ok)
        self.down_layout.setSpacing(10)

        self.down_widget = QWidget()
        self.down_widget.setStyleSheet('''QPushButton{background:grey;color:black;}
        QPushButton:hover{color:white;background:rgb(30,30,30);}
        QLineEdit{color:black;background:grey;}''')
        self.down_widget.setLayout(self.down_layout)


        self.right_layout.addWidget(self.temp)
        self.right_layout.addWidget(self.label_hint)
        self.right_layout.addWidget(self.lable_id)
        self.right_layout.addWidget(self.lable_name)
        self.right_layout.addWidget(self.down_widget)

        self.setLayout(self.right_layout)

        self.show()

def main2():
    app = QApplication(sys.argv)
    Ex = Right_widget()
        
    sys.exit(app.exec())

#创建一个线程，基于QThread,用于执行获取数据库内容操做
class MyThread(QThread):
    signal = pyqtSignal('PyQt_PyObject')

    def __init__(self,id):
        super(MyThread,self).__init__()
        self.id = id
        # print(id)
        self.op = databaseop()

    def run(self):
        res = self.op.get_id_info(self.id)
        # print(res)
        #结束运行时发送信号
        self.signal.emit(res)

#终端UI
class end_UI(QWidget):
    def __init__(self,parent = None):
        super(end_UI,self).__init__(parent)
        self.initUI()
    def paintEvent(self,event):
        qp = QPainter()
        qp.begin(self)
        self.drawLines(qp)
        qp.end()
 
    def drawLines(self, qp):
        pen = QPen(Qt.black, 2, Qt.SolidLine)
        pen.setColor(Qt.white)
        qp.setPen(pen)
        qp.drawLine(20, 61, 1200-20, 61)
     
    def initUI(self):
        self.window_pale = QPalette() 
        self.window_pale.setBrush(self.backgroundRole(),QBrush(QPixmap('./Icon/background_end.png'))) 
        self.setPalette(self.window_pale)
        # self.setStyleSheet('''background:rgb(135,70,125);''')
        self.width = 1200
        self.height = 1000
        self.setFixedSize(self.width,self.height)

        #设置面板和布局
        self.top_widget = QWidget(self)
        # self.top_widget.setStyleSheet('''background:white;''')
        self.bottom_widget = QWidget(self)
        # self.bottom_widget.setStyleSheet('''background:pink;''')


        self.right_widget = Right_widget(self)
        # self.right_widget.setStyleSheet('''background:white;''')

        self.left_widget = QWidget(self)
        # self.left_widget.setFixedWidth(660)
        # self.left_widget.setStyleSheet('''background:black;''')

        self.up_pic = QWidget(self.left_widget)
        # self.up_pic.setStyleSheet('''background:purple;''')

        self.down_pic = QWidget(self.left_widget)
        # self.down_pic.setStyleSheet('''background:purple;''')
        self.top_widget.setFixedHeight(60)
        self.up_pic.setFixedSize(720,360)
        self.down_pic.setFixedSize(720,360)




        self.layout_1 = QVBoxLayout()
        self.layout_1.addWidget(self.up_pic)
        self.layout_1.addWidget(self.down_pic)
        self.left_widget.setLayout(self.layout_1)

        self.layout_2 = QHBoxLayout()
        self.layout_2.addWidget(self.left_widget)
        self.layout_2.addWidget(self.right_widget)
        self.bottom_widget.setLayout(self.layout_2)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.top_widget)
        self.layout.addWidget(self.bottom_widget)

        self.setLayout(self.layout)
        self.layout.setSpacing(0)
        self.layout_1.setSpacing(0)
        self.layout_2.setSpacing(0)

        #在面板上添加其他东西
        #左边面板
        self.lable_up_pic = QLabel(self.up_pic)
        self.lable_down_pic = QLabel(self.down_pic)
        self.lable_up_pic.setAlignment(Qt.AlignCenter)
        self.lable_down_pic.setAlignment(Qt.AlignCenter)
        self.lable_up_pic.setFixedSize(640,360)
        self.lable_down_pic.setFixedSize(640,360)

        #上面面板
        self.top_layout = QHBoxLayout()
        self.lable_title = QLabel("人脸验证",self.top_widget)
        self.lable_time =  QLabel("2019/5/30",self.top_widget)
        self.lable_time.setAlignment(Qt.AlignRight)
        self.top_layout.addWidget(self.lable_title)
        self.top_layout.addWidget(self.lable_time)
        self.top_widget.setLayout(self.top_layout)
        self.top_widget.setStyleSheet('''font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
        font-size:30px;color:white;

        ''')
  

        self.setWindowTitle('终端')
        self.center()
        self.show()

    #控制窗口显示在屏幕中心的方法    
    def center(self):
        
        #获得窗口
        qr = self.frameGeometry()
        #获得屏幕中心点
        cp = QDesktopWidget().availableGeometry().center()
        #显示到屏幕中心
        qr.moveCenter(cp)
        self.move(qr.topLeft())

#继承终端UI实现相关逻辑
class end(end_UI):
    def __init__(self,parent = None):
        super(end,self).__init__(parent)
        self.initLogic()
        # self.initShowTimer()




    #初始化逻辑
    def initLogic(self):
        self.initCamera()
        self.initTime()
        self.right_widget.ok.clicked.connect(self.getOP)


    
    #初始化显示时间
    def initTime(self):
        self.timer_Time = QTimer()
        self.timer_Time.setInterval(100)
        self.timer_Time.start()
        self.timer_Time.timeout.connect(self.show_time)
    
    #获取当前时间并显示到相应标签
    def show_time(self):
        # 格式化成2016-03-20 11:45:39形式
        cur_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) 
        # print(cur_time)
        self.lable_time.setText(cur_time)    

    #创建新线程获取数据库信息
    def getOP(self):
        #判断是否有输入,没有输入直接退出
        if self.right_widget.get_id.text() == '':
            return
        #获取输入的账号信息
        self.id = self.right_widget.get_id.text()

        #实例化线程
        self.thread_getOP = MyThread(self.id)
        self.thread_getOP.signal.connect(self.judge_pass)
        self.thread_getOP.start()

    #判断输入是否正确，res为获取数据库信息线程发送的信号
    def judge_pass(self,res):
        if res == None:
            self.show_user_not_exist()
            return 
        print(res)
        self.show_info(res)
        # self.clear_all()

    #显示从数据库获取的用户身份信息
    def show_info(self,res):
        # self.timer_show.stop()
        self.right_widget.save_pic.setPixmap(QPixmap('Capture2.png').scaled(200,200))
        # self.right_widget.save_pic.setScaledContents (True)
        self.right_widget.label_hint.setText('人脸核验成功!')
        self.right_widget.lable_name.setText(res[1])
        self.right_widget.lable_id.setText(res[0])
        self.right_widget.get_id.clear()
        # time.sleep(3)
        self.timer_show = QTimer()
        self.timer_show.setInterval(1000)
        self.timer_show.timeout.connect(self.clear_all)
        self.timer_show.start()

    def show_user_not_exist(self):
        self.right_widget.label_hint.setText('用户不存在!')
        self.right_widget.get_id.clear()
        self.timer_show = QTimer()
        self.timer_show.setInterval(1000)
        self.timer_show.timeout.connect(self.clear_all)
        self.timer_show.start()
    #初始化所有的标签显示
    def clear_all(self):

        self.right_widget.label_hint.setText('人脸识别中...')
        self.right_widget.lable_name.setText('姓名')
        self.right_widget.lable_id.setText('学生号')
        self.right_widget.save_pic.setPixmap(self.right_widget.pixmap)
        # self.timer_show.


    #初始化相机
    def initCamera(self):
        self.timer_camera = QTimer()
        self.timer_camera.setInterval(30)
        self.timer_camera.start()
        self.timer_camera.timeout.connect(self.show_camera)

        self.CAM_num = 0
        self.capture = cv2.VideoCapture(self.CAM_num)

    #关闭程序时,清除相应的资源
    def closeEvent(self,event):
        self.timer_camera.stop()
        self.timer_Time.stop()
        self.capture.release()
        event.accept()

    #显示实时获取的图像，0.3秒刷新一次；保存获取的图像到'Capture1.png'和'Capture2.png'
    def show_camera(self):

        flag, self.image = self.capture.read()
        
        #获取捕获的图片
        cv2.imwrite("Capture1.png",self.image)

        show_image = cv2.resize(self.image, (640, 480))

        # img = cv2.imread("test.jpg")

        # 加载人脸特征，该文件在 python安装目录\Lib\site-packages\cv2\data 下
        face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        face_cascade.load('haarcascade_frontalface_default.xml')
        # 将读取的图像转为COLOR_BGR2GRAY，减少计算强度
        gray = cv2.cvtColor(show_image, cv2.COLOR_BGR2GRAY)

        # 检测出的人脸个数
        faces = face_cascade.detectMultiScale(gray, scaleFactor = 1.15, minNeighbors = 5, minSize = (5, 5))

        # print("Face : {0}".format(len(faces)))

        # 用矩形圈出人脸的位置
        for(x, y, w, h) in faces:
            cv2.rectangle(show_image, (x, y), (x + w, y + h),  (230,70,150), 2) 


        show_image = cv2.cvtColor(show_image, cv2.COLOR_BGR2RGB)

        #将捕获的图像保存到本地

        cv2.imwrite("Capture2.png",show_image)

        showImage = QtGui.QImage(show_image.data, show_image.shape[1], show_image.shape[0], QtGui.QImage.Format_RGB888)

        self.lable_up_pic.setPixmap(QtGui.QPixmap.fromImage(showImage))
        self.lable_down_pic.setPixmap(QtGui.QPixmap.fromImage(showImage))

    #Todo:将捕获的图片交给人脸识别模块进行同步处理，返回相应结果并在界面中做相应提示
    #Todo:将用户的识别信息提交到数据库，包括识别成功与识别失败
    #TODO:行为信息的日志上传
    #TODO:程序执行过程中可能出现的异常进行日志上传
def main():
    app = QApplication(sys.argv)
    Ex = end()
        
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
        