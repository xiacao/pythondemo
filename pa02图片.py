import urllib.request

response =urllib.request.urlopen('http://wx3.sinaimg.cn/mw600/0072bW0Xly1fonc54ncwmj30m80xcgtn.jpg')
#把地址转化为request对象
cat_img=response.read()

with open('D:\python\myspoils\cat_09.jpg','wb') as f:
    f.write(cat_img)
