# FileName : equipStatusDAO.py
# Author   : JiaDian
# DateTime : 2019/5/19 16:28 PM
# SoftWare : PyCharm

import pymysql
# username : jd
# password : jd20192019


class equipStatusDAO(object):
    ''' 定义一个 MySQL 操作类'''

    def __init__(self):
        '''初始化数据库信息并创建数据库连接'''
        self.db = pymysql.connect("cdb-g3b6mqvg.cd.tencentcdb.com", "jd", "jd20192019", "faceReg",10057 )


    def insertDb(self,sql, equiplist):
        ''' 插入数据库操作 '''

        self.cursor = self.db.cursor()

        try:
            # 执行sql
            tt = self.cursor.execute(sql,equiplist)  # 返回 插入数据 条数 可以根据 返回值 判定处理结果
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



    def addEquipStatus(self, EquipStatus):
        keyid = EquipStatus.keyid
        equipstatus = EquipStatus.equipstatus
        statusdate = EquipStatus.statusdate
        equipcodeid = EquipStatus.equipcodeid
        sql="INSERT INTO EQ_T_EQUIP_STATUS_INFO(KEYID, EQUIP_STATUS,STATUS_DATE,EQUIPCODE_ID)\
         VALUES (%s, %s,  %s, %s)"
        stulist=[keyid, equipstatus, statusdate, equipcodeid]
        self.insertDb(sql,  stulist)

    def getAllEquipStatusInfo(self):
        sql = "select * from EQ_T_EQUIP_STATUS_INFO"
        EquipStatusList = self.selectDbAll(sql)
        return EquipStatusList


    def writeEquipStatusIntoExecl(self):
        try:
            re = self.getAllEquipStatusInfo()
            import numpy as np
            import xlwt
            book = xlwt.Workbook()
            # 创建表单
            sheet1 = book.add_sheet(u'sheet1', cell_overwrite_ok=True)
            # 按i行j列顺序依次存入表格

            sheet1.write(0, 0, 'id')
            sheet1.write(0, 1, 'equipstatus')
            sheet1.write(0, 2, 'statusdate')
            sheet1.write(0, 3, 'equipcodeid')
            for i in range(len(re)):
                sheet1.write(i + 1, 0, re[i][0])
                sheet1.write(i + 1, 1, re[i][1])
                sheet1.write(i + 1, 2, re[i][2])
                sheet1.write(i + 1, 3, re[i][3])
                # 保存文件
            book.save('equipstatus.xls')
        except:
            import traceback
            traceback.print_exc()
            # 发生错误时会滚