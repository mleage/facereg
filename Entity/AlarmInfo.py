# FileName : AlarmInfo.py
# Author   : JiaDian
# DateTime : 2019/6/1 22:37 PM
# SoftWare : PyCharm


class Alarm(object):

    def __init__(self,id,regid,name, alarmstatus,alarminfo,accepttime\
                 ,picturepos,compvalue):
        self.id=id

        self.regid=regid

        self.name=name

        self.alarmstatus=alarmstatus

        self.alarminfo=alarminfo

        self.accepttime=accepttime

        self.picturepos=picturepos

        self.compvalue=compvalue
