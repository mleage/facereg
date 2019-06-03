# FileName : sysUserDAO.py
# Author   : JiaDian
# DateTime : 2019/6/1 16:28 PM
# SoftWare : PyCharm

import pymysql
from Entity import SystemUserInfo
# username : jd
# password : jd20192019



class sysUserDAO(object):
    ''' 定义一个 MySQL 操作类'''

    def __init__(self):
        '''初始化数据库信息并创建数据库连接'''
        self.db = pymysql.connect("cdb-g3b6mqvg.cd.tencentcdb.com", "jd", "jd20192019", "faceReg", 10057)


    def insertDb(self,sql, sysuserlist):
        ''' 插入数据库操作 '''

        self.cursor = self.db.cursor()

        try:
            # 执行sql
            tt = self.cursor.execute(sql,sysuserlist)  # 返回 插入数据 条数 可以根据 返回值 判定处理结果
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



    def addSingleSysUser(self, SystemUser):
        keyid = SystemUser.keyid
        useraccount = SystemUser.useraccount
        usertype = SystemUser.usertype
        userpassword = SystemUser.userpassword
        username = SystemUser.username
        nickname = SystemUser.nickname
        mobile = SystemUser.mobile
        useflag = SystemUser.useflag
        syslevel = SystemUser.syslevel
        sql="INSERT INTO XT_T_USER(KEYID, USER_ACCOUNT, USER_TYPE, USER_PASSWORD, \
        USER_NAME, NICKNAME, HANDSET, USER_FLAG, SYSLEVEL)\
         VALUES (%s,  %s, %s, %s, %s, %s, %s, %s, %s)"
        stulist=[keyid, useraccount, usertype, userpassword, username, nickname, mobile, useflag, syslevel]
        self.insertDb(sql,  stulist)

    def addMutiSysUser(self, SysUserList):
        for SystemUser in SysUserList:
            keyid = SystemUser.keyid
            useraccount = SystemUser.useraccount
            usertype = SystemUser.usertype
            userpassword = SystemUser.userpassword
            username = SystemUser.username
            nickname = SystemUser.nickname
            mobile = SystemUser.mobile
            useflag = SystemUser.useflag
            syslevel = SystemUser.syslevel
            sql = "INSERT INTO XT_T_USER(KEYID, USER_ACCOUNT, USER_TYPE, USER_PASSWORD, \
                 USER_NAME, NICKNAME, HANDSET, USER_FLAG, SYSLEVEL)\
                  VALUES (%s,  %s, %s, %s, %s, %s, %s, %s, %s)"
            stulist = [keyid, useraccount, usertype, userpassword, username, nickname, mobile, useflag,\
                       syslevel]
            self.insertDb(sql, stulist)

    def deleteSysUserByKeyId(self, keyid):
        keyid = keyid
        sql="DELETE FROM XT_T_USER WHERE KEYID = '%s'"%keyid
        self.deleteDb(sql)


    def deleteSysUserByUserAccount(self, useraccount):
        useraccount = useraccount
        sql = "DELETE FROM XT_T_USER WHERE USER_ACCOUNT = '%s'" % useraccount
        self.deleteDb(sql)

    def selectSysUserByKeyId(self, keyid):
        keyid = keyid
        sql = "select * from XT_T_USER where KEYID='%s'" % keyid
        SysUserList = self.selectDb(sql)
        return SysUserList

    def selectSysUserByKeyIdToStudent(self, keyid):
        keyid = keyid
        sql = "select * from XT_T_USER where KEYID='%s'" % keyid
        SysUserList = self.selectDb(sql)
        print(SysUserList)
        sys = SystemUserInfo.SystemUser(SysUserList[0],SysUserList[1],SysUserList[2],SysUserList[3],SysUserList[4],
                                        SysUserList[5],SysUserList[6],SysUserList[7],SysUserList[8])
        return sys

    def selectSysUserByUserAccount(self, useraccount):
        useraccount = useraccount
        sql = "select * from XT_T_USER where USER_ACCOUNT='%s'" % useraccount
        SysUserList = self.selectDb(sql)
        return SysUserList

    def selectSysUserByUserAccountToStudent(self, useraccount):
        useraccount = useraccount
        sql = "select * from XT_T_USER where USER_ACCOUNT='%s'" % useraccount
        SysUserList = self.selectDb(sql)
        sys = SystemUserInfo.SystemUser(SysUserList[0], SysUserList[1], SysUserList[2], SysUserList[3], SysUserList[4],
                                        SysUserList[5], SysUserList[6], SysUserList[7], SysUserList[8])
        return sys

    def updataSysUserInfoByKeyId(self, SystemUser,key_id):
        keyid = key_id
        mainid=SystemUser.keyid
        useraccount = SystemUser.useraccount
        usertype = SystemUser.usertype
        userpassword = SystemUser.userpassword
        username = SystemUser.username
        nickname = SystemUser.nickname
        mobile = SystemUser.mobile
        useflag = SystemUser.useflag
        syslevel = SystemUser.syslevel
        sql="UPDATE XT_T_USER SET KEYID='%s',USER_ACCOUNT='%s',USER_TYPE='%s',USER_PASSWORD='%s'\
        ,USER_NAME='%s',NICKNAME='%s',HANDSET='%s',USER_FLAG='%s',SYSLEVEL='%s' WHERE KEYID='%s'"%(mainid,useraccount,\
            usertype,userpassword,username,nickname,mobile,useflag,syslevel,keyid)
        self.updateDb(sql)

    def updataSysUserInfoByUserAccount(self, SystemUser, user_account):
        user_account = user_account
        mainid = SystemUser.keyid
        useraccount = SystemUser.useraccount
        usertype = SystemUser.usertype
        userpassword = SystemUser.userpassword
        username = SystemUser.username
        nickname = SystemUser.nickname
        mobile = SystemUser.mobile
        useflag = SystemUser.useflag
        syslevel = SystemUser.syslevel
        sql = "UPDATE XT_T_USER SET KEYID='%s',USER_ACCOUNT='%s',USER_TYPE='%s',USER_PASSWORD='%s'\
        ,USER_NAME='%s',NICKNAME='%s',HANDSET='%s',USER_FLAG='%s',SYSLEVEL='%s' WHERE USER_ACCOUNT='%s'" % (
        mainid, useraccount, \
        usertype, userpassword, username, nickname, mobile, useflag, syslevel, keyid, user_account)
        self.updateDb(sql)

    def getAllSysUserInfo(self):
        sql = "select * from XT_T_USER"
        SysUserList = self.selectDbAll(sql)
        return SysUserList