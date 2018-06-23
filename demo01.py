# _*_ coding:utf-8 _*_
import re
text=open("D:\python\myspoils\zhilian\index.html",'rb').read()

reg = re.compile(r'class="t1 ">.*? <a target="_blank" title="(.*?)".*? <span class="t2"><a target="_blank" title="(.*?)".*?<span class="t3">(.*?)</span>.*?<span class="t4">(.*?)</span>.*? <span class="t5">(.*?)</span>',re.S)
# 匹配换行符




findtext=re.findall(reg,str(text))

print(reg)
newtext=open(r"D:\python\myspoils\zhilian\b.txt","w")
newtext.writelines(line+"\n" for line in findtext)