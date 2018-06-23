import os

import getImage as gi


def openidentity():
    with open(r"allnumberbig.txt",'r') as f:
        number = f.read();
        number = number.split('\n')
        for each in number:
            #print(each)
            gi.getimage("image",each)


if "__main__" == __name__:
    openidentity()
