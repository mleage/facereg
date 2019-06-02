# FileName : checkDAO.py
# Author   : JiaDian
# DateTime : 2019/5/19 16:28 PM
# SoftWare : PyCharm

import pymysql
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

    def selectCheckByRegId(self, regid):
        regid = regid
        sql = "select * from PERSON_T_CHECKINFO where CI_REGID='%s'" % regid
        CheckList = self.selectDb(sql)
        return CheckList

