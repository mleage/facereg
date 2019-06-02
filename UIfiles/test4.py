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

class TopWidget(QWidget):
    def __init__(self,parent = None):
        super(TopWidget,self).__init__(parent)
        self.initUI()
    def initUI(self):
        self.resize(40,20)
        self.layout = QHBoxLayout()
        self.lable1 = QLabel(self)
        self.lable2 = QLabel(self)
        self.layout.addWidget(self.lable1)
        self.lable1.setAlignment(Qt.AlignCenter)
        self.lable2.setAlignment(Qt.AlignCenter)
        self.lable1.setPixmap(QPixmap('./Icon/minus_1.png').scaled(20,20))
        self.lable2.setPixmap(QPixmap('./Icon/times_1.png').scaled(20,20))

        self.layout.addWidget(self.lable2)
        self.layout.setSpacing(1)
        self.setLayout(self.layout)


        self.setStyleSheet('''QLabel#lable1{background:white;}
        QLabel:hover{background:red;}
        ''')
        self.setStyleSheet('''background:black;''')
        self.show()

def main():
    app = QApplication(sys.argv)
    ex = TopWidget()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()