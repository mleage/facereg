# FileName : CheckInfo.py
# Author   : JiaDian
# DateTime : 2019/6/1 22:37 PM
# SoftWare : PyCharm


class Check(object):

    def __init__(self,id,picture,regid,name,college,recogstatus,\
                 accepttime, picturepos,checked,compvalue):
        self.id = id

        self.picture = picture

        self.regid = regid

        self.name = name

        self.college = college

        self.recogstatus = recogstatus

        self.accepttime = accepttime

        self.picturepos = picturepos

        self.checked = checked

        self.compvalue = compvalue