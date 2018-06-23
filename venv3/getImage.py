import urllib.request
import os


def getimage(folder="image",number='2015052222'):
    #url = "http://dcard.zjhu.edu.cn/Zytk32Portal/default.aspx"
    head = {
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Cookie':'ASP.NET_SessionId=o5bq5n45uzxdkc45x2n0eo55',
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.36'
        }
    #req = urllib.request.Request(url,headers=head)
    #response = urllib.request.urlopen(req);
    #html = response.read();
    #image = html.decode('utf-8',errors='ignore')
    #print(image)
    #req2 = urllib.request.Request("http://dcard.hutc.zj.cn/Zytk32Portal/Cardholder/AccInfo.aspx",headers=head)
    #response2 = urllib.request.urlopen(req2)
    #html2 = response2.read();
    #image2 = html2.decode('utf-8',errors='ignore')
    #print(image2)
    url = "http://dcard.zjhu.edu.cn/Zytk32Portal/Cardholder/ShowImage.aspx?AccNum="+number
    req3 = urllib.request.Request(url,headers=head)
    response3 = urllib.request.urlopen(req3)
    html3 = response3.read()
    #print(url)
    with open(folder+"/"+number+".gif","wb") as f:
        f.write(html3)
        print("get image : " +number+" successed")

if '__main__' == __name__ :
    getimage()
