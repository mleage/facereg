# -*- coding: utf-8 -*-
import cv2

from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtWidgets import *

from PyQt5.QtCore import *

from PyQt5.QtGui import *

import os

import sys
from DATABASEOP import *
#创建一个线程，基于QThread,用于执行获取数据库内容操做
class MyThread(QThread):
    signal = pyqtSignal('PyQt_PyObject')

    def __init__(self,id):
        super(MyThread,self).__init__()
        self.id = id
        # print(id)
        self.op = databaseop()

    def run(self):
        res = self.op.get_user_info(self.id)
        # print(res)
        #结束运行时发送信号
        self.signal.emit(res)



#登录面板UI,无逻辑代码,逻辑代码需要继承后自己添加
class login_UI(QWidget):
    def __init__(self,parent = None):
        super(login_UI,self).__init__(parent)
        self.initUI()

    #初始化UI界面布局
    def initUI(self):
        self.width = 800
        self.height = 600
        self.setFixedSize(self.width,self.height)
        self.setSizePolicy(QSizePolicy.Fixed,QSizePolicy.Fixed)

        self.window_pale = QPalette() 
        self.window_pale.setBrush(self.backgroundRole(),QBrush(QPixmap('./Icon/background_end.png'))) 
        self.setPalette(self.window_pale)


        self.get_id = QLineEdit(self)
        self.get_pass = QLineEdit(self)
        self.get_id.setFrame(False)
        self.get_pass.setFrame(False)
        self.get_id.setMaxLength(20)
        self.get_pass.setMaxLength(20)

        self.get_id.setFixedSize(300,30)
        self.get_pass.setFixedSize(300,30)

        self.get_pass.setEchoMode(QLineEdit.Password)

        self.get_id.setPlaceholderText('input id')


        self.get_pass.setPlaceholderText('input password')

        self.ok = QPushButton('login in',self)

        self.ok.setFixedSize(300,40)

        self.label1 = QLabel(self)
        self.label2 = QLabel(self)
        self.label1.setAlignment(Qt.AlignCenter)
        self.label2.setAlignment(Qt.AlignCenter)



        self.label1.setPixmap(QPixmap('./Icon/user-fill.png').scaled(30,30))
        self.label2.setPixmap(QPixmap('./Icon/lock-fill.png').scaled(30,30))



        self.getinput_widget = QWidget(self)
        self.center_layout = QGridLayout()
        self.center_layout.setSpacing(10)
        self.center_layout.addWidget(self.label1,1,0)
        self.center_layout.addWidget(self.get_id,1,1)
        self.center_layout.addWidget(self.label2,2,0)
        self.center_layout.addWidget(self.get_pass,2,1)

        self.getinput_widget.setLayout(self.center_layout)

        #中间widget的总大小
        center_width = 360
        center_height = 90
        self.getinput_widget.setFixedSize(center_width,center_height)
        self.getinput_widget.move(self.width/2 - center_width/2,self.height/2 - center_height/2)

        self.ok.move(270,350)

        self.center()
        self.setWindowTitle('Login')
        self.show()

        self.setStyleSheet('''
        font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;font-size:20px;''')

    #控制窗口显示在屏幕中心的方法    
    def center(self):
        
        #获得窗口
        qr = self.frameGeometry()
        #获得屏幕中心点
        cp = QDesktopWidget().availableGeometry().center()
        #显示到屏幕中心
        qr.moveCenter(cp)
        self.move(qr.topLeft())

#重写消息提示框
class MyMessageBox(QMessageBox):
    def __init__(self):
        super(MyMessageBox,self).__init__()
        self.resize(200,200)
        self.window_pale = QPalette() 
        self.window_pale.setBrush(self.backgroundRole(),QBrush(QPixmap('./Icon/background_login.jpg')))
        self.setPalette(self.window_pale)
        self.setStyleSheet('''font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;font-size:50px;
        ''')

#继承登录界面，实现逻辑
class login(login_UI):
    def __init__(self):
        super(login,self).__init__()
        #设置风格

        #初始化事件
        self.initLogic()
    def initLogic(self):
        self.ok.clicked.connect(self.getOP)    

    def getOP(self):
        #判断是否有输入,没有输入直接退出
        if self.get_id.text() == '' or self.get_pass.text() == '':
            return
        #获取输入的账号信息
        self.id = self.get_id.text()
        self.password = self.get_pass.text()

        #实例化线程
        self.thread_getOP = MyThread(self.id)
        self.thread_getOP.signal.connect(self.judge_pass)
        self.thread_getOP.start()

    #判断输入是否正确，res为获取数据库信息线程发送的信号
    def judge_pass(self,res):
        #清除输入框内容
        self.clear()
        if res == None:
            MyMessageBox.about(self,"提示","用户不存在，请重试！")
            return 
        
        if res[2] != self.password:
            self.get_id.setText(self.id)
            MyMessageBox.about(self,"提示","密码错误，请重试！")
            return 
        MyMessageBox.about(self,"提示","登录成功！")
        #成功后自动退出
        self.close()
    def clear(self):
        self.get_id.clear()
        self.get_pass.clear()



def main():
    app = QApplication(sys.argv)
    log = login()
        
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
        