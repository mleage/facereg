# -*- coding: utf-8 -*-

import PyQt5

from PyQt5 import QtCore, QtGui, QtWidgets,QtMultimedia

from PyQt5.QtWidgets import *

from PyQt5.QtCore import *

from PyQt5.QtGui import *

from OtherWidget import *
#终端UI
class end_UI(QWidget):
    def __init__(self,parent = None):
        super(end_UI,self).__init__(parent)
        self.initUI()
        self.addTopWidget()
        self.setTopCss()
        self.addLeftWidget()
        self.setLeftCss()

    #最小化
    def minus(self):
        self.setWindowState(Qt.WindowMinimized)
    #在最上面添加一些控件
    def addTopWidget(self):
        self.topheight = 60
        self.top_widget.setFixedHeight(self.topheight)
        #添加退出按钮
        self.top_exit_button = QPushButton(self.top_widget)
        self.top_exit_button.setObjectName('exit')
        self.top_exit_button.setIcon(QIcon('./Icon/poweroff_1.png'))
        self.top_exit_button.clicked.connect(self.close)
        self.top_exit_button.setFixedSize(self.topheight,self.topheight)

        #添加最小化按钮
        self.top_minus_button = QPushButton(self.top_widget)
        self.top_minus_button.setObjectName('minus')
        self.top_minus_button.setIcon(QIcon('./Icon/minus_1.png'))
        self.top_minus_button.clicked.connect(self.minus)
        self.top_minus_button.setFixedSize(self.topheight,self.topheight)

        #设置Icon,四川大学logo
        self.icon = QLabel(self.top_widget)
        self.icon.setMargin(3)
        self.icon.setPixmap(QPixmap('./Icon/logo.jpg').scaled(self.topheight,self.topheight))

        #设置终端名字
        self.theme = QLabel(self.top_widget)
        self.theme.setMargin(2)
        self.theme.setStyleSheet('''background-color:#ff6e5c;font-size:30px;font-family:方正舒体;color:rgb(255,255,255);''')
        self.theme.setText("人卡核验终端")

        #设置显示时间标签
        self.lable_time =  QLabel("正在初始化...",self.top_widget)
        # self.lable_time.setAlignment(Qt.AlignRight)
        self.lable_time.setMargin(2)

        #设置布局，并将所有部件放置其中
        self.top_layout = QHBoxLayout()
        self.top_layout.setContentsMargins(0,0,0,0)
        self.top_layout.addWidget(self.icon)
        self.top_layout.addWidget(self.theme)
        self.top_layout.addStretch(1)
        self.top_layout.addWidget(self.lable_time)
        self.top_layout.addStretch(1)
        self.top_layout.addWidget(self.top_minus_button)
        self.top_layout.addWidget(self.top_exit_button)
        self.top_widget.setLayout(self.top_layout)
        pass 
    
    #设置顶部样式
    def setTopCss(self):
        self.top_widget.setStyleSheet('''
        QPushButton{   border-radius:1px;
                        background-color:#ff6e5c;}
        QPushButton:hover{   border-radius:1px;
                        background-color:#253e55;}

                        border-radius:1px;
                        background-color:#ff6e5c;
                       ''') 
        self.lable_time.setStyleSheet('''background-color:#ff6e5c;font-size:30px;font-family:方正舒体;color:rgb(255,255,255);''')
    
    #添加左边的控件
    def addLeftWidget(self):
        #设置左边面板大小
        self.left_height = 900 - 60
        self.left_width = 660
        self.left_widget.setFixedSize(self.left_width,self.left_height)

        #左边面板
        self.lable_up_pic = QLabel(self.left_widget)
        self.lable_down_pic = QLabel(self.left_widget)
        self.lable_up_pic.setFixedSize(640,360)#设置显示的图片大小
        self.lable_up_pic.setAlignment(Qt.AlignCenter)
        self.lable_up_pic.setStyleSheet('background-color:white;')
        self.lable_down_pic.setFixedSize(640,360)
        self.lable_down_pic.setAlignment(Qt.AlignCenter)
        self.lable_down_pic.setStyleSheet('background-color:white;')

        #设置左边面板布局
        self.left_layout = QVBoxLayout()
        self.left_layout.addWidget(self.lable_up_pic)
        self.left_layout.addWidget(self.lable_down_pic)
        self.left_widget.setLayout(self.left_layout)

        pass

    #设置左边的样式
    def setLeftCss(self):
        self.left_widget.setStyleSheet('''
        background-color:#253e55;
        ''')
        pass
        
    #初始化面板以及布局
    def initUI(self):
        #设置背景颜色
        pale = QPalette()
        pale.setColor(self.backgroundRole(), QColor('#253e55'))   # 设置背景颜色
        self.setPalette(pale)

        #设置界面大小
        self.width = 1500
        self.height = 900 + 60
        self.setFixedSize(self.width,self.height)

        #设置面板
        self.top_widget = QWidget(self)
        self.bottom_widget = QWidget(self)
        self.right_widget = Right_widget(self)
        self.left_widget = QWidget(self)


        #设置下面的布局
        self.layout_bottom = QHBoxLayout()
        self.layout_bottom.addWidget(self.left_widget)
        self.layout_bottom.addWidget(self.right_widget)
        self.bottom_widget.setLayout(self.layout_bottom)

        #设置整个界面的布局
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.top_widget)
        self.layout.addWidget(self.bottom_widget)
        self.setLayout(self.layout)

        #设置窗口格式
        self.setWindowFlags(Qt.FramelessWindowHint)
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
