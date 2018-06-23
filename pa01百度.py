import urllib.request
response=urllib.request.urlopen("http://baidu.com/")
html=response.read()
print(html)
