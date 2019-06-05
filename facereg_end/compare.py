#face++官方接口封装
#使用方法   传入需要对比的两张照片即可
import requests
from json import JSONDecoder
def compareIm(faceId1,faceId2):
    #传送两个本地图片地址
    try:
        #官方接口地址
        compare_url="https://api-cn.faceplusplus.com/facepp/v3/compare"
        #创建应用分配的key和secret
        key="FAsuHu5MZlaWl0PtgE9ZcqlQ3pcU5ort"
        secret="-c0c4A8MIrFNeiTwHdqIaENEdgCb1I9Q"
        #创建请求数据
        print("data")
        data={"api_key":key,"api_secret":secret}
        print("files")
        
        files={"image_file1":open(faceId1,"rb"),"image_file2":open(faceId2,"rb")}
       
        #通过接口发送请求
        print("request")
        response=requests.post(compare_url,data=data,files=files)
        print("ok")
        req_con=response.content.decode('utf-8')
        req_dict=JSONDecoder().decode(req_con)
        print(req_dict)
        
        #获得json文件里的confidence值，也就是相似度
        confidence=req_dict['confidence']
        # if confidence>75:
        print("图片相似度：",confidence)
        return confidence
    except Exception:
        pass
        print("无法识别")

if __name__ == '__main__':
    compareIm("../Capture1.png","Capture1.png")