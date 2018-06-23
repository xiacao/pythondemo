from aip import AipFace
""" 你的 APPID AK SK """
APP_ID = '10987260'
API_KEY = 'ktcQ6FvsLhgW1nwMm0BOYs3f'
SECRET_KEY = 'KCYGdlG7IuNeUnzLhjS20P6l0laovXQt '
client = AipFace(APP_ID, API_KEY, SECRET_KEY)



img1="D:\python\myspoils\\baifendemo\\1.jpg"
img2="D:\python\myspoils\\baifendemo\\2.jpg"
img3="D:\python\myspoils\\baifendemo\\3.jpg"
img4="D:\python\myspoils\\baifendemo\\4.jpg"
img5="D:\python\myspoils\\baifendemo\\5.jpg"
url_dict={"A某某":img1,"B某某":img2,"C某某":img3,"D某某":img4,"E某某":img5}

def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

for key,value in url_dict.items():
    # print(key,value)
    image = get_file_content(value)
    """ 调用人脸识别 """
    r = client.detect(image,options = {"face_fields":"age,gender,beauty,qualities"})
    #print(r["result"])
    for i in r["result"]:
        print("{} 颜值 {} 年龄 {} 性别 {}  ".format(key,i["beauty"],i["age"],i["gender"]))




