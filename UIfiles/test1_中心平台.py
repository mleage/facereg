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

#右中间的表格
class CenterTable(QTableWidget):
    def __init__(self,parent = None):
        super(CenterTable,self).__init__(parent)
        self.addInfo()
        self.initUI()
        self.setCss()
    
    def initUI(self):    
        # self.setFixedSize(1400,650)
        self.setFrameShadow(QFrame.Raised)
        # self.setFrameStyle(QFrame.Box)
        # self.setLineWidth(2)
        # self.setContentsMargins(2,2,2,2)
        # self.setViewportMargins(2,2,2,2)
        # self.setAutoScrollMargin(2)
        self.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.verticalHeader().setVisible(False)#隐藏列表头
        self.horizontalHeader().setVisible(True)#隐藏列表头
        #设置表格不能拖动
        self.horizontalHeader().setDisabled(True)
        self.verticalHeader().setDisabled(True)
        #

        self.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
        
        self.setAutoScroll(False)
        self.setVerticalScrollMode(QAbstractItemView.ScrollPerItem)
        self.verticalScrollBar().setCursor(Qt.PointingHandCursor)
        # self.horizontalHeader().(False)
        # self.show()
    
    #设置样式
    def setCss(self):

        self.verticalHeader().setStyleSheet('''''')

 
        self.horizontalHeader().setStyleSheet('''
        background-color:#ffffff;color:black;font-size:20px bold;font-family:隶书;

        
        ''')
        self.setStyleSheet('''QTableWidget{background-color:#ffffff;color:black;font-size:20px;font-family:隶书;}
        QTableWidget::item:selected { background: white;color:black;border:0px solid white; }
        QTableWidget::item:hover { background: #5bc0eb;border:0px solid white;color:white; }
        ''')
        self.setStyleSheet('''
        QPushButton{border:0px solid white}
        QPushButton:hover{background:#5bc0eb}
        ''')

    #修改表单内容为前一页
    def changeInfoLeft(self):
        if self.cur_page == 0:
            return
        self.cur_page -= 1
        self.showInfo()

    #修改表单内容为后一页
    def changeInfoRight(self):
        if self.cur_page < int(len(self.data) / self.info_perpage) - 1:
            self.cur_page += 1
            self.showInfo()
        elif self.cur_page == int(len(self.data) / self.info_perpage) - 1\
             and len(self.data) -  self.info_perpage*int(len(self.data) / self.info_perpage) != 0:
            self.changeInfoLastPage()
    
    #修改表单内容为第一页
    def changeInfoFirstPage(self):
        self.cur_page = 0
        for i in range(self.info_perpage):
            #在单元格加入控件
            newItem_check = QCheckBox()
            newItem_1 = QTableWidgetItem(self.data[i + self.cur_page*self.info_perpage][0])
            # newItem_1.setTextAlignment(Qt.AlignCenter)
            newItem_2 = QTableWidgetItem(self.data[i + self.cur_page*self.info_perpage][1])
            newItem_3 = QTableWidgetItem(self.data[i + self.cur_page*self.info_perpage][2])

            sex = "女"
            if self.data[i + self.cur_page*self.info_perpage][3] == 1:
                sex = "男"
            newItem_4 = QTableWidgetItem(sex)
            newItem_5 = QPushButton("修改")

            self.setCellWidget(i,0,newItem_check)
            self.setItem(i,1,newItem_1)
            self.setItem(i,2,newItem_2)
            self.setItem(i,3,newItem_3)
            self.setItem(i,4,newItem_4)
            self.setCellWidget(i,5,newItem_5) 
    
    #修改表单内容为最后一页
    def changeInfoLastPage(self):
        self.lastPageNumber = len(self.data) -  self.info_perpage*int(len(self.data) / self.info_perpage)
        print(self.lastPageNumber)
        if self.lastPageNumber == 0:
            return 
        self.cur_page = int(len(self.data) / self.info_perpage)
        self.setRowCount(self.lastPageNumber)
        for i in range(self.lastPageNumber):
            #在单元格加入控件
            newItem_check = QCheckBox()
            newItem_1 = QTableWidgetItem(self.data[i + self.cur_page*self.info_perpage][0])
            # newItem_1.setTextAlignment(Qt.AlignCenter)
            newItem_2 = QTableWidgetItem(self.data[i + self.cur_page*self.info_perpage][1])
            newItem_3 = QTableWidgetItem(self.data[i + self.cur_page*self.info_perpage][2])

            sex = "女"
            if self.data[i + self.cur_page*self.info_perpage][3] == 1:
                sex = "男"
            newItem_4 = QTableWidgetItem(sex)
            newItem_5 = QPushButton("修改")

            self.setCellWidget(i,0,newItem_check)
            self.setItem(i,1,newItem_1)
            self.setItem(i,2,newItem_2)
            self.setItem(i,3,newItem_3)
            self.setItem(i,4,newItem_4)
            self.setCellWidget(i,5,newItem_5) 
    
    #在表单中显示当前页面内容
    def showInfo(self):
        self.setRowCount(self.row)
        for i in range(self.info_perpage):
            #在单元格加入控件
            newItem_check = QCheckBox()
            newItem_1 = QTableWidgetItem(self.data[i + self.cur_page*self.info_perpage][0])
            # newItem_1.setTextAlignment(Qt.AlignCenter)
            newItem_2 = QTableWidgetItem(self.data[i + self.cur_page*self.info_perpage][1])
            newItem_3 = QTableWidgetItem(self.data[i + self.cur_page*self.info_perpage][2])

            sex = "女"
            if self.data[i + self.cur_page*self.info_perpage][3] == 1:
                sex = "男"
            newItem_4 = QTableWidgetItem(sex)
            newItem_5 = QPushButton("修改")

            self.setCellWidget(i,0,newItem_check)
            self.setItem(i,1,newItem_1)
            self.setItem(i,2,newItem_2)
            self.setItem(i,3,newItem_3)
            self.setItem(i,4,newItem_4)
            self.setCellWidget(i,5,newItem_5) 
  
    #设置表格相关属性并显示第一页
    def addInfo(self):
        self.info_perpage = 15
        #当前显示的页面,每一页包含10个数据
        self.cur_page = 0

        db = databaseop()
        self.data = db.get_all_user_info()
        # print(self.data)
        self.row = self.info_perpage
        self.column = len(self.data[0]) + 2

        self.setColumnCount(self.column)
        self.setRowCount(self.row)
    
        self.setHorizontalHeaderLabels(['选择',"id", "姓名", "密码","性别",'操作'])
        #显示表格内容
        self.showInfo()


class MainWindow(QWidget):
    def __init__(self,parent = None):
        super(MainWindow,self).__init__(parent)
        self.leftwidth = 200
        self.rightwidth = 1300
        self.topheight = 50
        self.otherheight = 850
        self.righttopheight = 100
        self.rightdownheight = 100
        self.rightcenterheight = 650
        self.initUI()
        self.addWidgetOfLeft()
        self.setTopCss()
        self.setLeftCss()
        self.addRightDownWidget()
        self.setRightDownCss()
        self.addRightTopWidget()
        self.setRightTopCss()
    #最小化
    def minus(self):
        self.setWindowState(Qt.WindowMinimized)
    #退出程序
    def exit(self):
        QMessageBox.question()
    #设置右下样式部件
    def setRightDownCss(self):
        self.right_downwidget.setStyleSheet('''
        QPushButton{background:white;color:black;border:1px solid grey;font-family:隶书;font-size:20px;}
        QPushButton:hover{background:#5bc0eb;color:white;}
        QLabel{background:#ffffff;color:black;font-family:隶书;font-size:20px;}
        ''')
    #设置顶部部件样式
    def setTopCss(self):
        self.topwidget.setStyleSheet('''
        QPushButton{   border-radius:1px;
                        background-color:#ff6e5c;}
        QPushButton:hover{   border-radius:1px;
                        border-left:2px solid red;
                        background-color:#253e55;}

                        border-radius:1px;
                        background-color:#ff6e5c;
                       ''')
    #添加左边部件
    def addWidgetOfLeft(self):
        title = ['  运行信息','  人员信息管理','  设备管理','  系统管理','  消息发布','  信息交互','  报表生成']
        Icons = ['./Icon/laptop.png','./Icon/user-circle_1.png','./Icon/terminal-fill.png','./Icon/resource.png','./Icon/news_1.png','./Icon/share.png','./Icon/file-fill.png']
        self.buttons = []
        for i in range(7):
            self.buttons.append(QPushButton(title[i],self.leftwidget))
            self.buttons[i].setFixedSize(200,100)
            self.buttons[i].setIcon(QIcon(Icons[i]))

        self.leftlayout = QVBoxLayout()
        for i in range(7):
            self.leftlayout.addWidget(self.buttons[i])

        self.leftlayout.setSpacing(10)
        self.leftlayout.setContentsMargins(5,0,0,0)
        self.leftwidget.setLayout(self.leftlayout)
    #设置左边部件样式
    def setLeftCss(self):
        self.leftwidget.setStyleSheet('''
            QPushButton{text-align:left; background-color:#253e55;color:grey;border:0px solid white;font-size:20px;font-family:隶书;}
            QPushButton:hover{background-color:#000000;border-left:10px solid white; color:white;font-size:22px;font-family:隶书;}

                border-radius:1px;
                background-color:#253e55;
        ''')
    #添加右上部件
    def addRightTopWidget(self):
        #五个，按钮，按钮，输入框输入框，按钮
        self.add_btn = QPushButton('添加',self.right_topwidget)
        self.delete_btn = QPushButton('删除',self.right_topwidget)
        self.get_id = QLineEdit(self.right_topwidget)
        self.get_id.setPlaceholderText('查询ID')
        self.get_name = QLineEdit(self.right_topwidget)
        self.get_name.setPlaceholderText('查询姓名')

        self.find_btn = QPushButton('查询',self.right_topwidget)
        self.right_topwidget_layout = QHBoxLayout()
        self.right_topwidget_layout.addWidget(self.add_btn)
        self.right_topwidget_layout.addWidget(self.delete_btn)
        self.right_topwidget_layout.addStretch(1)
        self.right_topwidget_layout.addWidget(self.get_id)
        self.right_topwidget_layout.addWidget(self.get_name)
        self.right_topwidget_layout.addStretch(1)
        self.right_topwidget_layout.addWidget(self.find_btn)
        self.right_topwidget.setLayout(self.right_topwidget_layout)
    #设置右上样式
    def setRightTopCss(self):
        self.right_topwidget.setStyleSheet('''
        QPushButton{background:#5bc0eb;color:white;font-size:20px;font-family:隶书;}
        QLineEdit{background:#ffffff;color:black;font-size:20px;font-family:隶书;}

        QPushButton:hover{}
        ''')
    #添加右下部件
    def addRightDownWidget(self):
        self.left_arrow = QPushButton(' < ',self.right_downwidget)
        self.right_arrow = QPushButton(' > ',self.right_downwidget)
        self.firstpage = QPushButton(' -首页 ',self.right_downwidget)
        self.lastpage = QPushButton(' -尾页 ',self.right_downwidget)
        self.show_page = QLabel(self.right_downwidget)
        self.show_page.setText(str(self.right_centertable.cur_page+1))
        self.right_downwidget_layout = QHBoxLayout()
        self.right_downwidget_layout.addStretch(1)
        self.right_downwidget_layout.addWidget(self.firstpage)
        # self.right_downwidget_layout.addStretch(1)
        self.right_downwidget_layout.addWidget(self.left_arrow)
        self.right_downwidget_layout.addStretch(1)
        self.right_downwidget_layout.addWidget(self.show_page)
        self.right_downwidget_layout.addStretch(1)
        self.right_downwidget_layout.addWidget(self.right_arrow)
        # self.right_downwidget_layout.addStretch(1)
        self.right_downwidget_layout.addWidget(self.lastpage)
        self.right_downwidget_layout.addStretch(1)
        self.right_downwidget.setLayout(self.right_downwidget_layout)

        self.left_arrow.clicked.connect(self.changeInfoLeft)
        self.right_arrow.clicked.connect(self.changeInfoRight)
        self.lastpage.clicked.connect(self.changeInfoLastPage)
        self.firstpage.clicked.connect(self.changeInfoFirstPage)
    
    def changeInfoFirstPage(self):
        self.right_centertable.changeInfoFirstPage()
        self.show_page.setText(str(self.right_centertable.cur_page+1))

    def changeInfoLastPage(self):
        self.right_centertable.changeInfoLastPage()
        self.show_page.setText(str(self.right_centertable.cur_page+1))

    def changeInfoLeft(self):
        self.right_centertable.changeInfoLeft()
        self.show_page.setText(str(self.right_centertable.cur_page+1))

    def changeInfoRight(self):
        self.right_centertable.changeInfoRight()
        self.show_page.setText(str(self.right_centertable.cur_page+1))


        pass
    #初始化UI
    def initUI(self):

        self.setWindowFlags(Qt.FramelessWindowHint   )
        self.setFixedSize(1500,900)
        self.setStyleSheet('''background-color:#ffffff;''')

        self.topwidget = QWidget(self)
        self.topwidget.setFixedSize(1500,self.topheight)

        #在最上面添加一些控件
        self.top_exit_button = QPushButton(self.topwidget)
        self.top_exit_button.setObjectName('exit')
        self.top_exit_button.setIcon(QIcon('./Icon/poweroff_1.png'))
        self.top_exit_button.clicked.connect(self.close)


        self.top_minus_button = QPushButton(self.topwidget)
        self.top_minus_button.setObjectName('minus')

        self.top_minus_button.setIcon(QIcon('./Icon/minus_1.png'))
        self.top_minus_button.clicked.connect(self.minus)
        
        self.top_exit_button.setFixedSize(self.topheight,self.topheight)
        self.top_minus_button.setFixedSize(self.topheight,self.topheight)

        self.icon = QLabel(self.topwidget)
        self.icon.setMargin(3)
        self.icon.setPixmap(QPixmap('./Icon/MyIcon.png').scaled(40,40))

        
        self.theme = QLabel(self.topwidget)
        self.theme.setMargin(2)
        self.theme.setStyleSheet('''background-color:#ff6e5c;font-size:30px;font-family:方正舒体;color:rgb(255,255,255);''')
        self.theme.setText("中心控制平台")


        self.top_layout = QHBoxLayout()
        self.top_layout.setContentsMargins(0,0,0,0)
        # self.top_layout.addStretch(1)
        self.top_layout.addWidget(self.icon)

        self.top_layout.addWidget(self.theme)

        self.top_layout.addStretch(1)

        self.top_layout.addWidget(self.top_minus_button)
        self.top_layout.addWidget(self.top_exit_button)
        self.topwidget.setLayout(self.top_layout)



        self.downwidget = QWidget(self)

        self.rightwidget = QWidget(self.downwidget)   
        self.leftwidget = QWidget(self.downwidget)

        self.leftwidget.setFixedSize(self.leftwidth,self.otherheight)
        self.leftwidget.setStyleSheet('''background-color:#253e55''')

        self.down_layout = QHBoxLayout()
        self.down_layout.setContentsMargins(0,0,0,0)
        self.down_layout.setSpacing(0)
        self.down_layout.addWidget(self.leftwidget)
        self.down_layout.addWidget(self.rightwidget)
        self.downwidget.setLayout(self.down_layout)

        self.right_topwidget = QWidget(self.rightwidget)
        self.right_topwidget.setFixedSize(self.rightwidth,self.righttopheight)
        self.right_topwidget.setStyleSheet('''background-color:#ffffff''')
        self.right_centertable = CenterTable(self.rightwidget)
        self.right_centertable.setFixedSize(self.rightwidth,self.rightcenterheight)
        
        self.right_downwidget = QWidget(self.rightwidget)
        self.right_downwidget.setFixedSize(self.rightwidth,self.rightdownheight)
        self.right_downwidget.setStyleSheet('''background-color:#ffffff''')

        self.right_layout = QVBoxLayout()
        self.right_layout.setContentsMargins(0,0,0,0)
        self.right_layout.setSpacing(0)
        self.right_layout.addWidget(self.right_topwidget)
        self.right_layout.addWidget(self.right_centertable)
        self.right_layout.addWidget(self.right_downwidget)
        self.rightwidget.setLayout(self.right_layout)

        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(0,0,0,0)
        self.layout.setSpacing(0)
        self.layout.addWidget(self.topwidget)
        self.layout.addWidget(self.downwidget)
        self.setLayout(self.layout)

        self.show()


def main():
    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()