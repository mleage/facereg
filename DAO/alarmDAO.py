# FileName : alarmDAO.py
# Author   : JiaDian
# DateTime : 2019/5/19 16:28 PM
# SoftWare : PyCharm

import pymysql
# username : jd
# password : jd20192019


class alarmDAO(object):
    ''' 定义一个 MySQL 操作类'''

    def __init__(self):
        '''初始化数据库信息并创建数据库连接'''
        self.db = pymysql.connect("cdb-g3b6mqvg.cd.tencentcdb.com", "jd", "jd20192019", "faceReg",10057 )


    def insertDb(self,sql, alarmlist):
        ''' 插入数据库操作 '''

        self.cursor = self.db.cursor()

        try:
            # 执行sql
            tt = self.cursor.execute(sql,alarmlist)  # 返回 插入数据 条数 可以根据 返回值 判定处理结果
            print(tt)
            self.db.commit()
        except ValueError:
            print(ValueError)
            # 发生错误时回滚
            self.db.rollback()
        finally:
            self.cursor.close()


    def deleteDb(self,sql):
        ''' 操作数据库数据删除 '''
        self.cursor = self.db.cursor()

        try:
            # 执行sql
            self.cursor.execute(sql)
            # tt = self.cursor.execute(sql) # 返回 删除数据 条数 可以根据 返回值 判定处理结果
            # print(tt)
            self.db.commit()
        except:
            # 发生错误时回滚
            self.db.rollback()
        finally:
            self.cursor.close()


    def updateDb(self,sql):
        ''' 更新数据库操作 '''

        self.cursor = self.db.cursor()

        try:
            # 执行sql
            self.cursor.execute(sql)
            # tt = self.cursor.execute(sql) # 返回 更新数据 条数 可以根据 返回值 判定处理结果
            # print(tt)
            self.db.commit()
        except:
            # 发生错误时回滚
            self.db.rollback()
        finally:
            self.cursor.close()


    def selectDb(self,sql):
        ''' 数据库查询 '''
        self.cursor = self.db.cursor()
        try:
            self.cursor.execute(sql) # 返回 查询数据 条数 可以根据 返回值 判定处理结果

            data = self.cursor.fetchone() # 返回所有记录列表

            return data
        except:
            print('Error: unable to fecth data')
        finally:
            self.cursor.close()

    def selectDbAll(self, sql):
        ''' 数据库查询 '''
        self.cursor = self.db.cursor()
        try:
            self.cursor.execute(sql)  # 返回 查询数据 条数 可以根据 返回值 判定处理结果

            data = self.cursor.fetchall()  # 返回所有记录列表

            return data
        except:
            print('Error: unable to fecth data')
        finally:
            self.cursor.close()

    def closeDb(self):
        ''' 数据库连接关闭 '''
        self.db.close()



    def addAlarmInfo(self, Alarm):
        id = Alarm.id
        regid = Alarm.regid
        name = Alarm.name
        alarmstatus = Alarm.alarmstatus
        alarminfo = Alarm.alarminfo
        accepttime = Alarm.accepttime
        picturepos = Alarm.picturepos
        compvalue = Alarm.compvalue
        sql="INSERT INTO PERSON_R_ALARM(ID, CI_REGID, CI_PSONNAME, \
        ALARMSTATUS, ALARMINFO, ACCEPTTIME, PICTUREPOS, COMPVALUE) VALUES (%s, %s,  %s, %s, %s, %s, %s, %s)"
        stulist=[id, regid, name, alarmstatus, alarminfo, accepttime, picturepos, compvalue]
        self.insertDb(sql,  stulist)


    def selectAlarmById(self, id):
        id = id
        sql = "select * from PERSON_R_ALARM where ID='%s'" % id
        AlarmList = self.selectDb(sql)
        return AlarmList

    def selectAlarmByRegId(self, regid):
        regid = regid
        sql = "select * from PERSON_R_ALARM where CI_REGID='%s'" % regid
        AlarmList = self.selectDb(sql)
        return AlarmList

    def deleteAlarmById(self, id):
        id = id
        sql="DELETE FROM PERSON_R_ALARM WHERE ID = '%s'"%id
        self.deleteDb(sql)


    def deleteAlarmByRegId(self, regid):
        regid = regid
        sql = "DELETE FROM PERSON_R_ALARM  WHERE CI_REGID = '%s'" % regid
        self.deleteDb(sql)

    def getAlarmInfo(self):
        sql = "select * from PERSON_R_ALARM"
        AlarmList = self.selectDbAll(sql)
        return AlarmList