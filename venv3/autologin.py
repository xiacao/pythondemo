import urllib.request
import json

def getConfineCode():

    url = 'http://dcard.zjhu.edu.cn/Zytk32Portal/'

    req = urllib.request.Request(url)
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.89 Safari/537.36')
    response = urllib.request.urlopen(req)

    html = response.read()
    html = html.decode('utf-8')
    #print(html)
    yzm = []
    a = html.find('src="images/')
    while a!=-1 :
         if str(html[a+12:a+13]).isdigit() :
              #print(html[a+12:a+13])
              yzm.append(html[a+12:a+13])
         a = html.find('src="images/',a+1)

    yzmzf = ''.join(yzm)
   # print(yzmzf)
    return yzmzf

def aotuLogin(username="2015283302",password="201937"):
    #confinecode = getConfineCode()
    #print(confinecode)
    url = 'http://dcard.zjhu.edu.cn/Zytk32Portal/Default.aspx'
    header = {
          'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.87 Safari/537.36',\
          'Referer':'http://dcard.zjhu.edu.cn/Zytk32Portal/'
          }
    data1 ={'UserLogin:txtUser':username,\
          'UserLogin:txtPwd':password,\

          'UserLogin:ddlPerson':'卡户'}
    data1 = json.dumps(data1)
    req = urllib.request.Request(url,headers=header,data=data1.encode('gb2312'),method='POST')
    response = urllib.request.urlopen(req)
    html = response.read()

    result = html.decode('utf-8',errors='ignore')
   # print(result)



if '__main__' == __name__ :
    aotuLogin()
