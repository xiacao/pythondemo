import urllib.request
import urllib.parse
import os
import http.cookiejar


def postdata(number='2015283316'):
    url = 'http://172.20.8.103/servlet/adminservlet'

    # cookie = http.cookiejar.CookieJar()    #作用未知
    # cookieProc = urllib.request.HTTPCookieProcessor(cookie)
    # openner = urllib.request.build_opener(cookieProc)
    # urllib.request.install_opener(openner)
    data1 = {'select': '2', \
             'userName': number, \
             'passwd': number}

    head = {

        'Host': '172.20.8.103', \
        'Origin': 'http://172.20.8.103', \
        'Referer': 'http://172.20.8.103/index.jsp', \
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.87 Safari/537.36', \
        }

    data1 = 'displayName=&displayPasswd=&select=2&submit.x=57&submit.y=12&operType=911&random_form=-5202932450791912540&userName=' + number + '&passwd=' + number
    req = urllib.request.Request('http://172.20.8.103/servlet/adminservlet', headers=head, data=data1.encode('utf-8'),
                                 method='POST')
    # print(req)
    response = urllib.request.urlopen(req)
    data2 = 'userName=' + number + '&passwd=' + number
    # 登录必须改cookies
    head2 = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8', \
             'Accept-Encoding': 'gzip, deflate, sdch', \
             'Accept-Language': 'zh-CN,zh;q=0.8', \
             'Connection': 'keep-alive', \
             'Cookie': 'JSESSIONID=CA40F89BAE95EBE1A2DE65ABE089686C', \
             'Host': '172.20.8.103', \
             'Upgrade-Insecure-Requests': '1', \
             'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.87 Safari/537.36}'}
    url2 = 'http://172.20.8.103/student/studentInfo.jsp?userName=' + number + '&passwd=' + number
    req2 = urllib.request.Request(url2, headers=head2, method='GET')
    response2 = urllib.request.urlopen(req2)
    html = response2.read()

    # data1 = 'displayName=&displayPasswd=&select=2&submit.x=55&submit.y=25&operType=911&random_form=5376445873113457738&userName=2015283316&passwd=2015283316'

    final = html.decode('utf-8', errors='ignore')
    # print(final)
    # print('getidentity('+number+')successed')
    return final


if '__main__' == __name__:
    postdata()

