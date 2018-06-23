import urllib.request

import urllib.parse
import json
import time
import random
import hashlib

content = input('请输入需要翻译的句子：')

url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'

###模拟浏览器
head={}
head['User-Agent']='Mozilla/5.0(Windows NT 6.3; WOW64) AppleWebKit/537.36(KHTML,like Gecko) Cheome/39.0.2171.65 Safari/537.36'
###


data = {}

u = 'fanyideskweb'
d = content
f = str(int(time.time()*1000) + random.randint(1,10))
c = 'rY0D^0\'nM0}g5Mm1z%1G4'

sign = hashlib.md5((u + d + f + c).encode('utf-8')).hexdigest()

data['i'] = content
data['from'] = 'AUTO'
data['to'] = 'AUTO'
data['smartresult'] = 'dict'
data['client'] = 'fanyideskweb'
data['salt'] = f
data['sign'] = sign
data['doctype'] = 'json'
data['version'] = '2.1'
data['keyfrom'] = 'fanyi.web'
data['action'] = 'FY_BY_CL1CKBUTTON'
data['typoResult'] = 'true'

data = urllib.parse.urlencode(data).encode('utf-8')


req=urllib.request.Request(url,data,head)
response=urllib.request.urlopen(req)
#r = urllib.request.urlopen(url,data)##这一句话可替代上面两句

html = response.read().decode('utf-8')

target = json.loads(html)

print('翻译结果是：%s'%(target['translateResult'][0][0]['tgt']))
#request = urllib.request.Request(url=url,data=data,method='POST')
#response = urllib.request.urlopen(request)

#print(response.read().decode('utf-8'))
#print(req.headers)