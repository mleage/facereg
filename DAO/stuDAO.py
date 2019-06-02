# FileName : stuDAO.py
# Author   : JiaDian
# DateTime : 2019/5/19 16:28 PM
# SoftWare : PyCharm

import pymysql
# username : jd
# password : jd20192019


class stuDAO(object):
    ''' 定义一个 MySQL 操作类'''

    def __init__(self):
        '''初始化数据库信息并创建数据库连接'''
        self.db = pymysql.connect("cdb-g3b6mqvg.cd.tencentcdb.com", "jd", "jd20192019", "faceReg",10057)


    def insertDb(self,sql, stulist):
        ''' 插入数据库操作 '''

        self.cursor = self.db.cursor()

        try:
            # 执行sql
            tt = self.cursor.execute(sql,stulist)  # 返回 插入数据 条数 可以根据 返回值 判定处理结果
            print(tt)
            self.db.commit()
        except ValueError:
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
            print("1")
            self.cursor.execute(sql)
           # tt = self.cursor.execute(sql) # 返回 更新数据 条数 可以根据 返回值 判定处理结果
            print("1")
            self.db.commit()
        except EnvironmentError:
            print(str(EnvironmentError))
            # 发生错误时回滚
            self.db.rollback()
            print("error")
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



    def addSingleStudent(self, Student):
        id = Student.id
        picture = Student.picture
        regId = Student.regId
        name = Student.name
        college = Student.college
        mentor = Student.mentor
        isreg = Student.isreg
        sex = Student.sex
        unitnum = Student.unitnum
        dormnum = Student.dormnum
        major = Student.major
        suit = Student.suit
        is_green = Student.is_green
        region = Student.region
        nation = Student.nation
        classid = Student.classid
        sql="INSERT INTO PERSON_T_REGINFO(CI_MAIN, CI_PICTURE, CI_REGID, CI_PSONNAME, \
        CI_COLLEGE, CI_MENTOR, IS_REG, CI_SEX, UNITNUM, DORMNUM, \
        `MAJOR`, SUITE, IS_GREEN, REGION, NATION, CLASSID) VALUES (%s, %s,  %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        stulist=[id, picture, regId, name, college, mentor, isreg, sex, unitnum, dormnum, major, suit, is_green, region, nation, classid]
        self.insertDb(sql,  stulist)

    def addMutiStudent(self, StudentList):
        for Student in StudentList:
         id = Student.id
         picture = Student.picture
         regId = Student.regId
         name = Student.name
         college = Student.college
         mentor = Student.mentor
         isreg = Student.isreg
         sex = Student.sex
         unitnum = Student.unitnum
         dormnum = Student.dormnum
         major = Student.major
         suit = Student.suit
         is_green = Student.is_green
         region = Student.region
         nation = Student.nation
         classid = Student.classid
         sql = "INSERT INTO PERSON_T_REGINFO(CI_MAIN, CI_PICTURE, CI_REGID, CI_PSONNAME, \
            CI_COLLEGE, CI_MENTOR, IS_REG, CI_SEX, UNITNUM, DORMNUM, \
            `MAJOR`, SUITE, IS_GREEN, REGION, NATION, CLASSID) VALUES (%s, %s,  %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
         stulist = [id, picture, regId, name, college, mentor, isreg, sex, unitnum, dormnum, major, suit, is_green,
                    region, nation, classid]
         self.insertDb(sql, stulist)

    def deleteStudentById(self, id):
        id = id
        sql="DELETE FROM PERSON_T_REGINFO WHERE CI_MAIN = '%s'"%id
        self.deleteDb(sql)


    def deleteStudentByRegId(self, regid):
        regid = regid
        sql = "DELETE FROM PERSON_T_REGINFO WHERE CI_REGID = '%s'" % regid
        self.deleteDb(sql)

    def selectStudentById(self, id):
        id=id
        sql="select * from PERSON_T_REGINFO where CI_MAIN='%s'" % id
        StudentList=self.selectDb(sql)
        return StudentList

    def selectStudentByRegId(self, regid):
        regid=regid
        sql = "select * from PERSON_T_REGINFO where CI_REGID='%s'" % regid
        StudentList = self.selectDb(sql)
        return StudentList

    def selectStudentByName(self, name):
        name=name
        sql = "select * from PERSON_T_REGINFO where CI_PSONNAME='%s'" % name
        StudentList = self.selectDb(sql)
        return StudentList


    def updataStudentInfoById(self, Student,id):
        id = id
        mainid=Student.id
        picture = Student.picture
        regId = Student.regId
        name = Student.name
        college = Student.college
        mentor = Student.mentor
        isreg = Student.isreg
        sex = Student.sex
        unitnum = Student.unitnum
        dormnum = Student.dormnum
        major = Student.major
        suit = Student.suit
        is_green = Student.is_green
        region = Student.region
        nation = Student.nation
        classid = Student.classid
        sql = "UPDATE PERSON_T_REGINFO SET CI_MAIN='%s',CI_PICTURE='%s', CI_REGID ='%s',CI_PSONNAME='%s', CI_COLLEGE='%s',\
        CI_MENTOR='%s',IS_REG='%s',CI_SEX='%s',UNITNUM='%s',DORMNUM='%s',`MAJOR`='%s', SUITE='%s',IS_GREEN='%s',REGION='%s',\
        NATION='%s',CLASSID='%s' WHERE CI_MAIN='%s'" % (mainid, picture, regId, name, college, mentor, isreg, sex, unitnum, dormnum, major, suit, is_green, region, nation, classid, id)
        self.updateDb(sql)

    def updataStudentInfoByRegId(self, Student, regid):
        regid = regid
        mainid = Student.id
        picture = Student.picture
        regId = Student.regId
        name = Student.name
        college = Student.college
        mentor = Student.mentor
        isreg = Student.isreg
        sex = Student.sex
        unitnum = Student.unitnum
        dormnum = Student.dormnum
        major = Student.major
        suit = Student.suit
        is_green = Student.is_green
        region = Student.region
        nation = Student.nation
        classid = Student.classid
        sql = "UPDATE PERSON_T_REGINFO SET CI_MAIN='%s',CI_PICTURE='%s', CI_REGID ='%s',CI_PSONNAME='%s', CI_COLLEGE='%s',\
           CI_MENTOR='%s',IS_REG='%s',CI_SEX='%s',UNITNUM='%s',DORMNUM='%s',`MAJOR`='%s', SUITE='%s',IS_GREEN='%s',REGION='%s',\
           NATION='%s',CLASSID='%s' WHERE CI_REGID='%s'" % (
        mainid, picture, regId, name, college, mentor, isreg, sex, unitnum, dormnum, major, suit, is_green, region,
        nation, classid, regid)
        self.updateDb(sql)
