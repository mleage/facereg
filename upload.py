import pymysql 
import os
import datetime
create_table_sql = """\
    CREATE TABLE checkinfo(
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    stuid VARCHAR(20),
    checkdate DATE,
    checkstate VARCHAR(255)
    )
    """
update_table_sql = """\
    UPDATE checkinfo SET checkstate = '{checkstate}' WHERE stuid = '{stuid}'
    """
insert_table_sql = """\
    INSERT INTO checkinfo(name,stuid, checkdate,checkstate)
    VALUES('{name}','{stuid}','{checkdate}','{checkstate}')
    """

query_table_sql = """\
    SELECT id, name, stuid, checkdate, checkstate
    FROM checkinfo 
    """

delete_table_sql = """\
    DELETE FROM checkinfo 
    """

drop_table_sql = """\
    DROP TABLE checkinfo
    """
#将本平台数据上传到数据库中
#如果表不存在，建一个(默认名为checkinfo)
def create_table():
    connection = pymysql.connect(
        host = "cdb-g3b6mqvg.cd.tencentcdb.com",
        port = 10057,
        user = "jd",
        database = "faceReg",
        password = "jd20192019",
        charset = "utf8")
    try:
        with connection.cursor() as cursor:
            print('--------------新建表--------------')
            cursor.execute(create_table_sql)
            connection.commit()
    finally:    
        connection.close()
    
if __name__ == '__create_table__':
    create_table()
#create_table()

#对数据库中的签到表进行更新，输入学号查找对象并更新签到状态
def update_table(checkstate, stuid):
    connection = pymysql.connect(
        host = "cdb-g3b6mqvg.cd.tencentcdb.com",
        port = 10057,
        user = "jd",
        database = "faceReg",
        password = "jd20192019",
        charset = "utf8")
    try:
        with connection.cursor() as cursor:
            print('--------------上传数据至数据库--------------')
            cursor.execute(
                update_table_sql.format(checkstate = checkstate, stuid = stuid))
            connection.commit()
    except Exception as e:
        connection.rollback()
        print('更新失败，事务回滚！失败原因：',e)
    else:
        connection.commit()
        print("更新数据成功")
    connection.close()
if __name__ == '__update_table__':
    update_table(checkstate, name)
#update_table("???", "2017141461037")

#向数据库的表插入数据，输入姓名、学号，自动插入学生信心并设置签到状态
def insert_table(name, stuid, checkstate):
    connection = pymysql.connect(
        host = "cdb-g3b6mqvg.cd.tencentcdb.com",
        port = 10057,
        user = "jd",
        database = "faceReg",
        password = "jd20192019",
        charset = "utf8")
    try:
        with connection.cursor() as cursor:
            print('--------------更新数据--------------')
            cursor.execute(insert_table_sql.format(name=name, stuid=stuid, checkdate=datetime.date.today(),checkstate=checkstate))
            connection.commit()
    except Exception as e:
        connection.rollback()
        print('插入数据失败，事务回滚！失败原因：',e)
    else:
        connection.commit()
        print("插入数据成功", '上传数据',cursor.rowcount,'行')
    connection.close()
    
if __name__ == '__insert_table__':
    insert_table(name, stuid, checkstate)
#insert_table("gwf","2017141461008", "dead")
#insert_table("wqy","2017141461037", "dead")
#insert_table("fxn","2017141461164", "good")

#向数据库查询内容，实现与中心平台信息交互
def query_table():
    connection = pymysql.connect(
        host = "cdb-g3b6mqvg.cd.tencentcdb.com",
        port = 10057,
        user = "jd",
        database = "faceReg",
        password = "jd20192019",
        charset = "utf8")
    with connection.cursor() as cursor:
        print('--------------查询数据--------------')
        cursor.execute(query_table_sql)
        results = cursor.fetchall()
        print(f'checkid\tname\tstuid\t\tcheckdate\tcheckstate')
        for row in results:
            print(row[0], row[1], row[2], row[3], row[4], sep='\t')
    connection.close()
    
if __name__ == '__query_table__':
    query_table()
query_table()

#如果数据出错，删除数据内容
def delete_table():
    connection = pymysql.connect(
        host = "cdb-g3b6mqvg.cd.tencentcdb.com",
        port = 10057,
        user = "jd",
        database = "faceReg",
        password = "jd20192019",
        charset = "utf8")
    with connection.cursor() as cursor:
        print('--------------清除数据--------------')
        cursor.execute(delete_table_sql)
        connection.commit()
    connection.close()
#delete_table()

#如果出错的数据已上传到数据库，删除数据库中的数据表单
def drop_table():
    connection = pymysql.connect(
        host = "cdb-g3b6mqvg.cd.tencentcdb.com",
        port = 10057,
        user = "jd",
        database = "faceReg",
        password = "jd20192019",
        charset = "utf8")
    with connection.cursor() as cursor:
        print('--------------删除数据表单--------------')
        cursor.execute(drop_table_sql)
        connection.commit()
    connection.close()
#drop_table()