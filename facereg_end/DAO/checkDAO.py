# FileName : checkDAO.py
# Author   : JiaDian
# DateTime : 2019/5/19 16:28 PM
# SoftWare : PyCharm

import pymysql
from Entity import CheckInfo
# username : jd
# password : jd20192019


class checkDAO(object):
    ''' 定义一个 MySQL 操作类'''

    def __init__(self):
        '''初始化数据库信息并创建数据库连接'''
        self.db = pymysql.connect("cdb-g3b6mqvg.cd.tencentcdb.com", "jd", "jd20192019", "faceReg",10057 )


    def insertDb(self,sql, checklist):
        ''' 插入数据库操作 '''

        self.cursor = self.db.cursor()

        try:
            # 执行sql
            tt = self.cursor.execute(sql,checklist)  # 返回 插入数据 条数 可以根据 返回值 判定处理结果
            print(tt)
            self.db.commit()
        except:
            print("error")
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

    def selectDbAll(self,sql):
        ''' 数据库查询 '''
        self.cursor = self.db.cursor()
        try:
            self.cursor.execute(sql) # 返回 查询数据 条数 可以根据 返回值 判定处理结果

            data = self.cursor.fetchall() # 返回所有记录列表

            return data
        except:
            print('Error: unable to fecth data')
        finally:
            self.cursor.close()

    def closeDb(self):
        ''' 数据库连接关闭 '''
        self.db.close()



    def addCheckInfo(self, Check):
        id = Check.id
        picture = Check.picture
        regid = Check.regid
        name = Check.name
        college = Check.college
        recogstatus = Check.recogstatus
        accepttime = Check.accepttime
        picturepos = Check.picturepos
        checked = Check.checked
        compvalue = Check.compvalue
        sql="INSERT INTO PERSON_T_CHECKINFO(CI_ID, CI_PICTURE, CI_REGID, CI_PSONNAME, \
        CI_COLLEGE, CI_RECOGSTATUS, ACCEPTTIME, PICTUREPOS, CI_CHECKED, COMPVALUE) VALUES (%s, %s,  %s, %s, %s, %s, %s, %s, %s, %s)"
        stulist=[id, picture, regid, name, college, recogstatus, accepttime, picturepos, checked, compvalue]
        self.insertDb(sql,  stulist)


    def selectCheckById(self, id):
        id = id
        sql = "select * from PERSON_T_CHECKINFO where CI_ID='%s'" % id
        CheckList = self.selectDb(sql)
        return CheckList

    def selectCheckByIdToStudent(self, id):
        id = id
        sql = "select * from PERSON_T_CHECKINFO where CI_ID='%s'" % id
        CheckList = self.selectDb(sql)
        check=CheckInfo.Check(CheckList[0],CheckList[1],CheckList[2],CheckList[3],CheckList[4],CheckList[5],CheckList[6]
                              ,CheckList[7],CheckList[8],CheckList[9])
        return check

    def selectCheckByRegId(self, regid):
        regid = regid
        sql = "select * from PERSON_T_CHECKINFO where CI_REGID='%s'" % regid
        CheckList = self.selectDb(sql)
        return CheckList

    def selectCheckByRegIdToStudent(self, regid):
        regid = regid
        sql = "select * from PERSON_T_CHECKINFO where CI_REGID='%s'" % regid
        CheckList = self.selectDb(sql)
        check = CheckInfo.Check(CheckList[0], CheckList[1], CheckList[2], CheckList[3], CheckList[4], CheckList[5],
                                CheckList[6]
                                , CheckList[7], CheckList[8], CheckList[9])
        return check

    def getAllCheckInfo(self):
        sql = "select * from PERSON_T_CHECKINFO"
        CheckList = self.selectDbAll(sql)
        return CheckList

    def writeCheckIntoExcel(self):
        try:
            re = self.getAllCheckInfo()
            import numpy as np
            import xlwt
            book = xlwt.Workbook()
            # 创建表单
            sheet1 = book.add_sheet(u'sheet1', cell_overwrite_ok=True)
            # 按i行j列顺序依次存入表格

            sheet1.write(0, 0, 'id')
            sheet1.write(0, 1, 'picture')
            sheet1.write(0, 2, 'regid')
            sheet1.write(0, 3, 'name')
            sheet1.write(0, 4, 'college')
            sheet1.write(0, 5, 'recogstatus')
            sheet1.write(0, 6, 'accepttime')
            sheet1.write(0, 7, 'picturepos')
            sheet1.write(0, 8, 'checked')
            sheet1.write(0, 9, 'compvalue')
            for i in range(len(re)):
                sheet1.write(i + 1, 0, re[i][0])
                sheet1.write(i + 1, 1, re[i][1])
                sheet1.write(i + 1, 2, re[i][2])
                sheet1.write(i + 1, 3, re[i][3])
                sheet1.write(i + 1, 4, str(re[i][4]))
                sheet1.write(i + 1, 5, str(re[i][5]))
                sheet1.write(i + 1, 6, str(re[i][6]))
                sheet1.write(i + 1, 7, re[i][7])
                sheet1.write(i + 1, 8, str(re[i][8]))
                sheet1.write(i + 1, 9, str(re[i][9]))
                # 保存文件
            book.save('check.xls')
        except:
            import traceback
            traceback.print_exc()
            # 发生错误时会滚