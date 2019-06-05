# -*- coding: utf-8 -*-

import PyQt5

from PyQt5 import QtCore, QtGui, QtWidgets,QtMultimedia

from PyQt5.QtWidgets import *

from PyQt5.QtCore import *

from PyQt5.QtGui import *
import DAO,Entity
from DAO import stuDAO,equipStatusDao

from DAO import checkDAO

from Entity import StudentInfo,CheckInfo,EquipStatusInfo
from compare import *
import time

import datetime

import math

#用于异步获取对比结果的线程
class RegThread(QThread):
    signal = pyqtSignal('PyQt_PyObject')

    def __init__(self,file1,file2):
        super(RegThread,self).__init__()
        self.file1 = file1
        self.file2 = file2

    def run(self): 
        self.result = compareIm(self.file1,self.file2)
        print('this is in thread result: %lf',self.result)
        self.signal.emit(self.result)
        print("人脸识别线程结束")

#创建一个用于播报语音的线程类
class AudioThread(QThread):
    def __init__(self,type):
        super(AudioThread,self).__init__()
        self.name = type
        self.filepath1 = r'./audio/not_exist.mp3'
        self.filepath2 = r'./audio/done.mp3'
        self.filepath3 = r'./audio/false.mp3'
        self.filepath4 = r'./audio/has_done.mp3'
    def run(self):
        filepath = ''
        if self.name == 1:
            filepath = self.filepath1
        elif self.name == 2:
            filepath = self.filepath2
        elif self.name == 3:
            filepath = self.filepath3
        else:
            filepath = self.filepath4

        self.player = QtMultimedia.QMediaPlayer()
        url = PyQt5.QtCore.QUrl.fromLocalFile(filepath)
        content = PyQt5.QtMultimedia.QMediaContent(url)
        self.player.setMedia(content)
        self.player.setVolume(50)
        self.player.play()   
        print("语音播报线程结束")


#创建一个线程，基于QThread,用于执行获取数据库内容操做
class DatabaseThread(QThread):
    signal = pyqtSignal('PyQt_PyObject')

    def __init__(self,id):
        super(DatabaseThread,self).__init__()
        self.id = id
        print(id)
        self.op = stuDAO.stuDAO()
    def run(self):
        res = self.op.selectStudentById(self.id)

        #结束运行时发送信号
        self.signal.emit(res)
        print("获取数据库线程结束")

#创建一个用于上传验证结果的线程,参数为上传类型(成功,失败),要上传的学生信息
class UploadThread(QThread):
    signal = pyqtSignal('PyQt_PyObject')

    def __init__(self,type,stu_info,confidence1):
        super(UploadThread,self).__init__()
        #学生信息
        self.cur_stu_info = stu_info
        self.type = type    
        self.confidence1 = confidence1

    def run(self):
        #根据上传类型进行上传
        if self.type == 1:
            self.upload_done()
            self.update_stu_info_isreg()#更新是否注册信息

        elif self.type == 0:
            self.upload_false()
        print("上传验证结果线程结束")

    #核验成功时上传核验信息
    def upload_done(self):
        id = self.cur_stu_info.id
        picture = self.cur_stu_info.picture
        regid = self.cur_stu_info.regId
        name = self.cur_stu_info.name
        college = self.cur_stu_info.college
        recogstatus = '成功'
        time = datetime.datetime.now()
        time = str(time.year) + '-' + str(time.month) + '-' +  str(time.day)
        accepttime = time
        # print(accepttime)
        picturepos = self.cur_stu_info.picture
        checked = '未知'
        compvalue = math.floor(self.confidence1)
        checkinfo = CheckInfo.Check(id,picture,regid,name,college,recogstatus,\
            accepttime,picturepos,checked,compvalue)
        db = checkDAO.checkDAO()
        db.addCheckInfo(checkinfo)
        print("核验信息上传成功!")
    
    #核验失败时上传核验信息
    def upload_false(self):
        id = self.cur_stu_info.id
        picture = self.cur_stu_info.picture
        regid = self.cur_stu_info.regId
        name = self.cur_stu_info.name
        college = self.cur_stu_info.college
        recogstatus = '失败'
        time = datetime.datetime.now()
        time = str(time.year) + '-' + str(time.month) + '-' +  str(time.day)
        accepttime = time
        # print(accepttime)
        picturepos = self.cur_stu_info.picture
        checked = '未知'
        compvalue = math.floor(self.confidence1)
        checkinfo = CheckInfo.Check(id,picture,regid,name,college,recogstatus,\
            accepttime,picturepos,checked,compvalue)
        db = checkDAO.checkDAO()
        db.addCheckInfo(checkinfo)
        print("核验信息上传成功!")

    #更新学生信息为已经注册
    def update_stu_info_isreg(self):
        self.cur_stu_info.isreg = 1
        db = stuDAO.stuDAO()
        db.updataStudentInfoById(self.cur_stu_info,self.cur_stu_info.id)
        print("注册信息已上传")

#创建一个用于上传设备状态线程,参数为要上传的keyid和codeid
class UploadDeviceThread(QThread):
    signal = pyqtSignal('PyQt_PyObject')

    def __init__(self,keyid,equipcodeid):
        super(UploadDeviceThread,self).__init__()
        self.keyid = keyid
        self.equipcodeid = equipcodeid  

    def run(self):
        #开始上传
        self.upload_devices_info()
        print("上传本地设备信息线程结束")
    def upload_devices_info(self):
        equipstatus = '1'

        time = datetime.datetime.now()
        time = str(time.year) + '-' + str(time.month) + '-' +  str(time.day)
        statusdate = time

        equipcodeid = self.equipcodeid        
        device_info = EquipStatusInfo.EquipStatus(equipstatus,statusdate,equipcodeid)
        db = equipStatusDao.equipStatusDAO()
        db.addEquipStatus(device_info)
        print("设备信息上传成功!")  
    
