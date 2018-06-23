import autologins as atl
#import fakeip
import re
import time
def writedown(xuehao):
     count = 0
     news = atl.postdata(xuehao)
     #print(news)
     findnews = re.findall(r'<td.+?bgcolor="#FFFFFF".+?</td>',news)
     #should change you own folder by .txt
     print(findnews)
     with open(r'2016identity.txt','a+') as f:
          for each in findnews :

               if count%2 == 0 :
                    print(each.split('&nbsp;')[-2]+'\t')
                    f.write(each.split('&nbsp;')[-2]+'\t')
               if count%2 == 1 :
                    xx=re.findall(r'&nbsp;.+?</td>',each)[0][6:-5]
                    f.write(xx+'\t')
                    print(xx+'\t')
               count+=1
               if count>7:
                    f.write('\n')
                    print('getidentity('+xuehao+')successed')
                    break

def rundown():
     #should enter you won filename by .txt
     with open(r'2016qztempnumber.txt','r') as q :
          studentnum = q.read()
          studentnum = studentnum.split('\n')
          for eachone in studentnum :
               writedown(eachone)
               #time.sleep(1)


if __name__=='__main__':
     rundown()
     #writedown('2015283316')
