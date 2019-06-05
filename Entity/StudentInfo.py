# FileName : StudentInfo.py
# Author   : JiaDian
# DateTime : 2019/5/19 16:48 PM
# SoftWare : PyCharm


class Student(object):

    def __init__(self, id, picture, regId, name, college, \
                 mentor, isreg,  sex, \
                 unitnum, dormnum, major, \
                 suit, is_green, region, nation, classid):
        self.id = id

        self.picture = picture

        self.regId = regId

        self.name = name

        self.college = college

        self.mentor = mentor

        self.isreg = isreg

        self.sex=sex

        self.unitnum = unitnum

        self.dormnum = dormnum

        self.major = major

        self.suit = suit

        self.picturepos = ''

        self.is_green = is_green

        self.is_cloth = 0

        self.region = region

        self.nation = nation

        self.classid = classid