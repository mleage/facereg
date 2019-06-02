# FileName : CheckInfo.py
# Author   : JiaDian
# DateTime : 2019/6/1 22:37 PM
# SoftWare : PyCharm


class Check(object):

    def __init__(self,id,picture,regid,name,college,recogstatus,\
                 accepttime, picturepos,checked,compvalue,face_x,face_y,\
                 face_width,face_height):
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

        self.face_x = face_x

        self.face_y = face_y

        self.face_width = face_width

        self.face_height = face_height