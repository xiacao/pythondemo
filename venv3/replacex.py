import re

#this python function can change you identity number form 'X' to '0'

def transport(folder):
     with open(folder,'r') as  f:
          getn = f.read()
          print(getn)
          
     getm = getn.replace('X','0')
     print(getm)

     with open(folder,'w') as  f:
          f.write(getm)

#enter you filename
transport('folder.txt')
