# FileName : test.py
# Author   : JiaDian
# DateTime : 2019/5/19 23:11 PM
# SoftWare : PyCharm
from Entity import StudentInfo
from Entity import SystemUserInfo
from Entity import EquipStatusInfo
from Entity import CheckInfo
from Entity import AlarmInfo
from DAO import alarmDAO
from DAO import checkDAO
from DAO import equipStatusDao
from DAO import stuDAO
from DAO import sysUserDAO


if __name__ == '__main__':

    studao = stuDAO.stuDAO()
    stu = StudentInfo.Student("123","123","123","123","123","123","123","123","123","123","123","123","123","123","123","123")
    stu.id = "12345"
    studao.updataStudentInfoById(stu,'123456')
    stu2=studao.selectStudentById('12345')
    print(stu2)


