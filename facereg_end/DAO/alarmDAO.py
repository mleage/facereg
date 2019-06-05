# FileName : alarmDAO.py
# Author   : JiaDian
# DateTime : 2019/5/19 16:28 PM
# SoftWare : PyCharm

import pymysql
from Entity import AlarmInfo
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

    def selectAlarmByIdToStudent(self, id):
        id = id
        sql = "select * from PERSON_R_ALARM where ID='%s'" % id
        AlarmList = self.selectDb(sql)
        alarm=AlarmInfo.Alarm(AlarmList[0],AlarmList[1],AlarmList[2],AlarmList[3],AlarmList[4],AlarmList[5],AlarmList[6],AlarmList[7])
        return alarm

    def selectAlarmByRegId(self, regid):
        regid = regid
        sql = "select * from PERSON_R_ALARM where CI_REGID='%s'" % regid
        AlarmList = self.selectDb(sql)
        return AlarmList

    def selectAlarmByRegIdToStudent(self, regid):
        regid = regid
        sql = "select * from PERSON_R_ALARM where CI_REGID='%s'" % regid
        AlarmList = self.selectDb(sql)
        alarm = AlarmInfo.Alarm(AlarmList[0], AlarmList[1], AlarmList[2], AlarmList[3], AlarmList[4], AlarmList[5],
                                AlarmList[6], AlarmList[7])
        return alarm

    def deleteAlarmById(self, id):
        id = id
        sql="DELETE FROM PERSON_R_ALARM WHERE ID = '%s'"%id
        self.deleteDb(sql)


    def deleteAlarmByRegId(self, regid):
        regid = regid
        sql = "DELETE FROM PERSON_R_ALARM  WHERE CI_REGID = '%s'" % regid
        self.deleteDb(sql)

    def getAllAlarmInfo(self):
        sql = "select * from PERSON_R_ALARM"
        AlarmList = self.selectDbAll(sql)
        return AlarmList

    def writeAlarmIntoExcel(self):
        try:
            re = self.getAllAlarmInfo()
            import numpy as np
            import xlwt
            book = xlwt.Workbook()
            # 创建表单
            sheet1 = book.add_sheet(u'sheet1', cell_overwrite_ok=True)
            # 按i行j列顺序依次存入表格

            sheet1.write(0, 0, 'id')
            sheet1.write(0, 1, 'regid')
            sheet1.write(0, 2, 'name')
            sheet1.write(0, 3, 'alarmstatus')
            sheet1.write(0, 4, 'alarminfo')
            sheet1.write(0, 5, 'accepttime')
            sheet1.write(0, 6, 'picturepos')
            sheet1.write(0, 7, 'compvalue')
            for i in range(len(re)):
                sheet1.write(i + 1, 0, re[i][0])
                sheet1.write(i + 1, 1, re[i][1])
                sheet1.write(i + 1, 2, re[i][2])
                sheet1.write(i + 1, 3, re[i][3])
                sheet1.write(i + 1, 4, str(re[i][4]))
                sheet1.write(i + 1, 5, str(re[i][5]))
                sheet1.write(i + 1, 6, str(re[i][6]))
                sheet1.write(i + 1, 7, re[i][7])
                # 保存文件
            book.save('alarm.xls')
        except:
            import traceback
            traceback.print_exc()
            # 发生错误时会滚