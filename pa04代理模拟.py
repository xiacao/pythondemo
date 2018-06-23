import  random
import  urllib.request



url='http://www.whatismyip.com.tw'
###
   ### 使用代理自定义的IP
###
iplist=['112.228.161.57:8118','125.126.164.21:34592','122.72.18.35:80','163.125.151.124:9999','114.250.25.19:80']

proxy_support=urllib.request.ProxyHandler({'http':random.choice(iplist)})

opener=urllib.request.build_opener(proxy_support)

###
### 模拟浏览器header
###
opener.addheaders=[('User-Agent','Mozilla/5.0(Windows NT 6.3; WOW64) AppleWebKit/537.36(KHTML,like Gecko) Cheome/39.0.2171.65 Safari/537.36')]

urllib.request.install_opener(opener)

response=urllib.request.urlopen(url)
html=response.read().decode('utf-8')

print(html)