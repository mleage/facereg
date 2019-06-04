# FileName : stuDAO.py
# Author   : JiaDian
# DateTime : 2019/5/19 16:28 PM
# SoftWare : PyCharm

import pymysql
from Entity import StudentInfo
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

    def selectStudentByIdToStudent(self, id):
        id = id
        sql = "select * from PERSON_T_REGINFO where CI_MAIN='%s'" % id
        StudentList = self.selectDb(sql)
        stu = StudentInfo.Student(StudentList[0], StudentList[1], StudentList[2], StudentList[3], StudentList[4],
                                  StudentList[5], \
                                  StudentList[7], StudentList[9], StudentList[10], StudentList[11], StudentList[12],
                                  StudentList[13], \
                                  StudentList[14], StudentList[16], StudentList[17], StudentList[18])
        return stu

    def selectStudentByRegId(self, regid):
        regid=regid
        sql = "select * from PERSON_T_REGINFO where CI_REGID='%s'" % regid
        StudentList = self.selectDb(sql)
        return StudentList

    def selectStudentByRegIdToStudent(self, regid):
        regid = regid
        sql = "select * from PERSON_T_REGINFO where CI_REGID='%s'" % regid
        StudentList = self.selectDb(sql)
        stu = StudentInfo.Student(StudentList[0], StudentList[1], StudentList[2], StudentList[3], StudentList[4],
                                  StudentList[5], \
                                  StudentList[7], StudentList[9], StudentList[10], StudentList[11], StudentList[12],
                                  StudentList[13], \
                                  StudentList[14], StudentList[16], StudentList[17], StudentList[18])
        return stu

    def selectStudentByName(self, name):
        name=name
        sql = "select * from PERSON_T_REGINFO where CI_PSONNAME='%s'" % name
        StudentList = self.selectDb(sql)
        return StudentList

    def selectStudentByName(self, name):
        name = name
        sql = "select * from PERSON_T_REGINFO where CI_PSONNAME='%s'" % name
        StudentList = self.selectDb(sql)
        stu = StudentInfo.Student(StudentList[0], StudentList[1], StudentList[2], StudentList[3], StudentList[4],
                                  StudentList[5], \
                                  StudentList[7], StudentList[9], StudentList[10], StudentList[11], StudentList[12],
                                  StudentList[13], \
                                  StudentList[14], StudentList[16], StudentList[17], StudentList[18])
        return stu

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

    def getAllStudentInfo(self):
        sql = "select * from PERSON_T_REGINFO"
        StudentList = self.selectDbAll(sql)
        return StudentList

    def writeStudentIntoExecl(self):
        try:
            re = self.getAllStudentInfo()
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
            sheet1.write(0, 5, 'mentor')
            sheet1.write(0, 6, 'isreg')
            sheet1.write(0, 7, 'sex')
            sheet1.write(0, 8, 'unitnum')
            sheet1.write(0, 9, 'dormnum')
            sheet1.write(0, 10, 'major')
            sheet1.write(0, 11, 'suit')
            sheet1.write(0, 12, 'is_green')
            sheet1.write(0, 13, 'region')
            sheet1.write(0, 14, 'nation')
            sheet1.write(0, 15, 'classid')
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
                sheet1.write(i + 1, 10, str(re[i][10]))
                sheet1.write(i + 1, 11, str(re[i][11]))
                sheet1.write(i + 1, 12, str(re[i][12]))
                sheet1.write(i + 1, 13, str(re[i][13]))
                sheet1.write(i + 1, 14, str(re[i][14]))
                sheet1.write(i + 1, 15, str(re[i][15]))
                # 保存文件
            book.save('student.xls')
        except:
            import traceback
            traceback.print_exc()
            # 发生错误时会滚
