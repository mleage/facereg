# -*- coding: utf-8 -*-
import cv2

from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtWidgets import *

from PyQt5.QtCore import *

from PyQt5.QtGui import *

import os

import sys
import pymysql

class databaseop():
    def __init__(self):
        self.name = 'root'
        self.password = '...iloveilove520'
        self.database = 'user_login'
        self.host = 'localhost'

    #获取所有的用户基本信息，通过学号获取，返回所有匹配的结果(可能为空)
    def get_user_info(self,id,table = 'user_info'):
        sql = '''select * from %s where user_id = %s'''%(table,str(id))

        db = pymysql.connect(self.host,self.name,self.password, self.database)
        cursor = db.cursor()

        cursor.execute(sql)

        res = cursor.fetchone()

        cursor.close()
        db.close()

        return res

    #获取所有的用户基本信息，返回所有匹配的结果(可能为空)
    def get_all_user_info(self,table = 'user_info'):
        sql = '''select * from %s'''%(table)

        db = pymysql.connect(self.host,self.name,self.password, self.database)
        cursor = db.cursor()

        cursor.execute(sql)

        res = cursor.fetchall()

        cursor.close()
        db.close()

        return res

    #获取身份证信息，通过身份证号获取，返回所有匹配的结果(可能为空)
    def get_id_info(self,id,table = 'id_info'):
        sql = '''select * from %s where id = %s'''%(table,id)

        db = pymysql.connect(self.host,self.name,self.password, self.database)
        cursor = db.cursor()

        cursor.execute(sql)

        res = cursor.fetchone()

        cursor.close()
        db.close()

        return res

    #上传用户登录行为
    def upload_behavior_info(self,id,name,success,table = 'user_behavior_info'):
        sql = '''insert into %s (user_id,user_name,login_time,login_success) values ('%s','%s',%s,%s)'''%(table,id,name,'now()',(success))
        print(sql)
        db = pymysql.connect(self.host,self.name,self.password, self.database)
        cursor = db.cursor()
        try:
            cursor.execute(sql)
            db.commit()
        except:
            db.rollback()
        cursor.close()
        db.close()

    #获取所有用户行为信息
    def get_all_user_behavior_info(self,table = 'user_behavior_info'):
        sql = '''select * from %s'''%(table)

        db = pymysql.connect(self.host,self.name,self.password, self.database)
        cursor = db.cursor()

        cursor.execute(sql)

        res = cursor.fetchall()

        cursor.close()
        db.close()

        return res
            
def main():
    OP = databaseop()
    
    info = OP.get_user_info('1844101043')

    print(info)

if __name__ == '__main__':
    main()