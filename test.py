import pymysql
import os
import datetime
import winsound
#系统初始化
def global_initialization():
    #检查网络连接状态
    print("正在检查网络连接")
    exit_code = os.system('ping www.baidu.com')
    if exit_code:
        raise Exception('网络连接失败')

    #检查数据库连接状态
    connect = pymysql.connect(
        host = "cdb-g3b6mqvg.cd.tencentcdb.com",
        port = 10057,
        user = "jd",
        database = "faceReg",
        password = "jd20192019",
        charset = "utf8")
    print("数据库连接成功")
    
    try:
        winsound.PlaySound('*', winsound.SND_ALIAS)
    except RuntimeError as e:
        print('麦克风连接失败,错误原因：', e)
    else:
        print("麦克风连接成功")
    
    #import faceReg
    print("人脸识别库装入成功")
    
if __name__ == '__global_initialization__':
    global_initialization()

#global_initialization()
