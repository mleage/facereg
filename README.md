# facereg

#### 运行这些界面需要导入的包：

>import cv2
>
>from PyQt5 import QtCore, QtGui, QtWidgets
>
>from PyQt5.QtWidgets import *
>
>from PyQt5.QtCore import *
>
>from PyQt5.QtGui import *
>
>import os
>
>import time
>
>import sys
>
>from DATABASEOP import *

可通过 pip install 安装cv2 和 pyqt5,详情可百度

##### 其中DATABASEOP是我本地测试的数据库操作，本项目实际操作需要连接贾典的数据库操作模块，若果运行有问题，可以将相关数据库操作删除再运行。



### 运行视图展示

##### 登录到中心平台

![](效果展示/登录.png)

##### 中心平台UI（有待更新）

![](效果展示/中心平台.png)

##### 终端UI(只需要人脸识别包便可以进行识别了)

![](效果展示/终端.png)


数据库操作目录结构说明：
entity是实体类，为各个数据表的实体对象，每个属性对应表中的一个栏位
DAO为持久层，也就是数据库操作层，里面封装了对应表项的增删改查方法
其中只有系统用户和学生信息具有完整的增删改查方法，其他日志类型的数据表
缺少修改方法
具体使用方法见test文件夹，使用时先创建相应的实体类，在创建对应的DAO对象
便可以用DAO中的方法来连接并操作数据库，具体方法的参数可以先看代码，有时间会更新
参数的详细注释
