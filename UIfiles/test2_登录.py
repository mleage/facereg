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

# class MyLineEdit(QLineEdit):
#     def __init__(self,parent = None):
#         super(MyLineEdit,self).__init__(parent)
#         # self.setFocusPolicy(Qt.NoFocus)
#         # self.setAlignment(Qt.AlignCenter)

#     def textChanged(self,event):
#         print('fuck')
#         if self.text() == '':
#             self.setAlignment(Qt.AlignCenter)
#         else:self.setAlignment(Qt.AlignLeft)
#     def focusInEvent(self,event):
#         if self.text() == '':
#             self.setAlignment(Qt.AlignCenter)
#         else: self.setAlignment(Qt.AlignLeft)
        
#     def focusOutEvent(self,event):
#         if self.text() == '':
#             self.setAlignment(Qt.AlignCenter)

#登录面板UI,无逻辑代码,逻辑代码需要继承后自己添加
class login_UI(QWidget):
    def __init__(self,parent = None):
        super(login_UI,self).__init__(parent)
        self.initUI()

    def initUI(self):
        self.width = 800
        self.height = 600
        self.setFixedSize(self.width,self.height)
        self.setSizePolicy(QSizePolicy.Fixed,QSizePolicy.Fixed)

        self.window_pale = QPalette() 
        self.window_pale.setBrush(self.backgroundRole(),QBrush(QPixmap('./Icon/background_login.jpg'))) 
        self.setPalette(self.window_pale)

        self.center_widget = QWidget(self)
        center_width = 300
        center_height = 200
        self.center_widget.setFixedSize(center_width,center_height)
        self.center_widget.move(self.width/2 - center_width/2,self.height/2 - center_height/2)

        self.layout = QVBoxLayout()

        self.get_id = QLineEdit(self)
        self.get_pass = QLineEdit(self)
        self.get_id.setFrame(False)
        self.get_pass.setFrame(False)
        self.get_id.setMaxLength(20)
        self.get_pass.setMaxLength(20)

        self.get_id.setFixedSize(300,40)
        self.get_pass.setFixedSize(300,40)

        self.get_pass.setEchoMode(QLineEdit.Password)
        # self.get_pass.textChanged.connect(self.change_align_pass)
        # self.get_pass.focusInEvent().connect(self.change_align_pass)
        self.get_id.setPlaceholderText('input id')
        # self.get_pass.setAlignment(Qt.AlignCenter)
        # self.get_id.setAlignment(Qt.AlignCenter)
        # self.get_id.textChanged.connect(self.change_align_id)


        self.get_pass.setPlaceholderText('input password')

        self.ok = QPushButton('login in',self)
        self.ok.setStyleSheet('''background:lightgrey''')
        self.ok.setWindowOpacity(0.8)

        self.ok.setFixedSize(300,50)

        self.layout.addWidget(self.get_id)
        self.layout.addWidget(self.get_pass)
        self.layout.addWidget(self.ok)

        self.center_widget.setLayout(self.layout)

        self.center()
        self.setWindowTitle('Login')
        self.show()
    # def change_align_id(self):
    #     self.get_id.setAlignment(Qt.AlignLeft)
    # def change_align_pass(self):
    #     self.get_pass.setAlignment(Qt.AlignLeft)
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
        self.setStyleSheet('''
        font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;font-size:20px;
        ''')
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
        