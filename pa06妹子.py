import requests
#import urllib3
import time
from bs4 import BeautifulSoup
#import re
from selenium import webdriver
#from selenium.webdriver.common.keys import Keys



###
''' 爬取煎蛋妹子图
    源码来源：https://www.jianshu.com/p/4654d201988d
    git：https://link.jianshu.com/?t=https%3A%2F%2Fgithub.com%2Faszt%2Fjiandan-gril
'''
###



Directory = 'D:\python\myspoils\mm\m'
base_url = "http://jandan.net/ooxx/page-"
path = "D:\python\za\chromedriver.exe"
driver = webdriver.Chrome(executable_path=path)
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'
}
img_url = []
print("请输入要爬取的页面范围（1-100）：\n")
sta = int(input("请输入开始页码："))
send = int(input("请输入结束页码："))

urls = ["http://jandan.net/ooxx/page-{}#comments".format(str(i)) for i in range(sta, send)]

def getImg():###保存
    n = 1
    for url in img_url:
        print('第' + str(n) + ' 张', end='')
        timename=str(time.time())
        timename=timename.replace('.','')
        timename=timename[7:]
        with open(Directory + timename+url[-5:], 'wb') as f:
            f.write(requests.get(url).content)
        print('...OK!')
        n = n+1

def getImgUrl(url):###获取url解析
    driver.get(url)
    data = driver.page_source
    soup = BeautifulSoup(data, "html.parser")  # 解析网页
    images = soup.select("a.view_img_link")  # 定位元素
    for i in images:
        z = i.get('href')
        if str('gif') in str(z):
            pass
        else:
            http_url = "http:" + z
            img_url.append(http_url)
            print(http_url)


if __name__ == "__main__":
    for url in urls:
        getImgUrl(url)
    getImg()
    print("完成！！！！！*-*")

