# -*- coding: utf-8 -*-

import PyQt5

from PyQt5 import QtCore, QtGui, QtWidgets,QtMultimedia

from PyQt5.QtWidgets import *

from PyQt5.QtCore import *

from PyQt5.QtGui import *
#右边面板
class Right_widget(QWidget):
    def __init__(self,parent = None):
        super(Right_widget,self).__init__(parent)
        self.initUI()
        # self.initShowPic()

    #动态显示图片
    def initShowPic(self):
        self.pics = []
        self.pics.append(QPixmap('./Icon/head_3.jpg'))
        self.pics.append(QPixmap('./Icon/head_4.jpg'))
        self.pics.append(QPixmap('./Icon/head_5.jpg'))
        self.pics.append(QPixmap('./Icon/head_6.jpg'))
        self.pics.append(QPixmap('./Icon/head_7.jpg'))
        self.pics.append(QPixmap('./Icon/head_8.jpg'))
        self.pics.append(QPixmap('./Icon/head_9.jpg'))
        self.pics.append(QPixmap('./Icon/head_10.jpg'))
        self.pics.append(QPixmap('./Icon/head_11.jpg'))
        self.curPic = 0
        self.picNum = 9
        self.timer = QTimer()
        self.timer.setInterval(10)
        self.timer.timeout.connect(self.changePic)
        self.timer.start()

    
    #修改图片
    def changePic(self):
        if self.curPic == self.picNum - 1:
            self.curPic = 0
        else:
            self.curPic += 1
        self.save_pic2.setPixmap(self.pics[self.curPic].scaled(200,200))

    #画图事件,画出标签下面的白线
    def paintEvent(self,event):
        qp = QPainter()
        qp.begin(self)
        self.drawLines(qp)
        qp.end()
 
    #在界面上画出标签下划线
    def drawLines(self, qp):
        pen = QPen(Qt.black, 2, Qt.SolidLine)
        pen.setColor(Qt.white)
        qp.setPen(pen)
        qp.drawLine(50, 485, 700, 485)
        qp.drawLine(50, 640, 700, 640)
    
    #初始化界面
    def initUI(self):
        self.setStyleSheet('''font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
        font-size:30px;color:white;''')

        #两个提示图案
        self.save_pic = QLabel(self)
        self.save_pic.setStyleSheet('background:rgb(30,30,30);')

        self.save_pic2 = QLabel(self)
        self.save_pic2.setStyleSheet('background:rgb(30,30,30);')

        self.save_pic.setFixedSize(200,200)        
        self.save_pic2.setFixedSize(200,200)

        self.pixmap = QPixmap('./Icon/default_head.png')
        self.pixmap  = self.pixmap.scaled(200,200)

        self.pixmap2 = QPixmap('./Icon/head_3.jpg')
        self.pixmap2  = self.pixmap2.scaled(200,200)

        self.save_pic.setPixmap(self.pixmap)
        self.save_pic2.setPixmap(self.pixmap2.scaled(200,200))

        self.layout_save_pic = QHBoxLayout()
        self.layout_save_pic.addWidget(self.save_pic)
        self.layout_save_pic.addWidget(self.save_pic2)

        #作为两幅图像的临时面板
        self.temp = QWidget()
        self.temp.setLayout(self.layout_save_pic)

        #添加中间的提示部件
        self.label_hint = QLabel('人脸识别中...',self)
        self.label_hint.setStyleSheet('''color:#ff6e5c;font-size:40;''')
        self.label_hint.setAlignment(Qt.AlignCenter)
        self.lable_id = QLabel('学号',self)
        self.lable_id.setAlignment(Qt.AlignCenter)
        self.lable_name = QLabel('姓名',self)
        self.lable_name.setAlignment(Qt.AlignCenter)

        #获取身份证号输入
        self.get_id = QLineEdit(self)
        self.get_id.setFixedSize(400,40)
        self.get_id.setPlaceholderText('请输入身份证号')
        self.get_id.setMaxLength(18)
        self.ok = QPushButton("&确定",self)

        #对获取输入按钮和确认按钮布局
        self.down_layout = QHBoxLayout()
        self.down_layout.addWidget(self.get_id)
        self.down_layout.addWidget(self.ok)
        self.down_layout.setSpacing(10)

        #作为临时面板
        self.down_widget = QWidget()
        self.down_widget.setStyleSheet('''QPushButton{background:grey;color:black;}
        QPushButton:hover{color:white;background:rgb(30,30,30);}
        QLineEdit{color:black;background:white;}''')
        self.down_widget.setLayout(self.down_layout)

        #设置整体的布局
        self.right_layout = QVBoxLayout()
        self.right_layout.setSpacing(10)
        self.right_layout.addWidget(self.temp)
        self.right_layout.addWidget(self.label_hint)
        self.right_layout.addWidget(self.lable_id)
        self.right_layout.addWidget(self.lable_name)
        self.right_layout.addWidget(self.down_widget)
        self.setLayout(self.right_layout)
