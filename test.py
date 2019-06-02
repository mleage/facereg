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
from DAO import equipStatusDAO
from DAO import stuDAO
from DAO import sysUserDAO


if __name__ == '__main__':

    equipstatusdao = equipStatusDAO.equipStatusDAO()
    equ = EquipStatusInfo.EquipStatus("123","1","2019-6-2","123")

    alarmdao=alarmDAO.alarmDAO()
    alarm=AlarmInfo.Alarm("123","123","123","123","123","2019-6-2","123","123")

    checkdao=checkDAO.checkDAO()
    check=CheckInfo.Check("123","123","123","123","123","123","2019-6-2","123","123","123")
    checkdao.addCheckInfo(check)

