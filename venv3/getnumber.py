import os

with open(r'2016qztempnumber.txt','w+') as f:
     #for first in range(2016,2017):
          first=201
     #for second in range(21,37):
          second=5052
          for third in range(1,5):
                    for number in range(1,40):
                         
                         if number<10 :
                              coun = '0'+str(number)
                         else :
                              coun = str(number)
                         if second<10 :
                              sec = '0'+str(second)
                         else :
                              sec = str(second)
                         realnumber = str(first)+sec+str(third)+coun
                         f.write(realnumber+'\n')
