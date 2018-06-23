import turtle 

def row(x, y):    #行
    t.setheading(0)
    t.up()
    t.setposition((x,y))
    t.down()
    t.forward(STEP_LENGTH)
    

def col(x, y):
    t.setheading(270)
    t.up()
    t.setposition((x,y))
    t.down()
    t.forward(STEP_LENGTH)
def drawzero(x,y):
    row(x,y)
    col(x,y)
    col(x+STEP_LENGTH,y)
    col(x+STEP_LENGTH,y-STEP_LENGTH)
    col(x,y-STEP_LENGTH)
    row(x,y-STEP_LENGTH*2)
    

def drawone(x,y):
    col(x+STEP_LENGTH,y)
    col(x+STEP_LENGTH,y-STEP_LENGTH)

def drawtwo(x,y):
    row(x,y)
    col(x+STEP_LENGTH,y)
    row(x,y-STEP_LENGTH)
    col(x,y-STEP_LENGTH)
    row(x,y-STEP_LENGTH*2)
 
def drawthree(x,y):
    row(x,y)
    col(x+STEP_LENGTH,y)
    row(x,y-STEP_LENGTH)
    col(x+STEP_LENGTH,y-STEP_LENGTH)
    row(x,y-STEP_LENGTH*2)

def drawfour(x,y):
    col(x,y)
    row(x,y-STEP_LENGTH)
    col(x+STEP_LENGTH,y)
    col(x+STEP_LENGTH,y-STEP_LENGTH)

def drawfive(x,y):
    row(x,y)
    col(x,y)
    row(x,y-STEP_LENGTH)
    col(x+STEP_LENGTH,y-STEP_LENGTH)
    row(x,y-STEP_LENGTH*2)

def drawsix(x,y):
    row(x,y)
    col(x,y)
    row(x,y-STEP_LENGTH)
    col(x+STEP_LENGTH,y-STEP_LENGTH)
    row(x,y-STEP_LENGTH*2)
    col(x,y-STEP_LENGTH)

def drawseven(x,y):
    row(x,y)
    col(x+STEP_LENGTH,y)
    col(x+STEP_LENGTH,y-STEP_LENGTH)

def draweight(x,y):
    row(x,y)
    col(x,y)
    col(x+STEP_LENGTH,y)
    row(x,y-STEP_LENGTH)
    col(x+STEP_LENGTH,y-STEP_LENGTH)
    row(x,y-STEP_LENGTH*2)
    col(x,y-STEP_LENGTH)

def drawnine(x,y):
    row(x,y)
    col(x,y)
    col(x+STEP_LENGTH,y)
    row(x,y-STEP_LENGTH)
    col(x+STEP_LENGTH,y-STEP_LENGTH)
    row(x,y-STEP_LENGTH*2)

def main():
    date = input("输入日期:")
    for i in range(len(date)):
        if date[i]<'0' or date[i]>'9':
            continue
        if date[i]=='0':
            drawzero(-400+60*int(i),-40)
        elif date[i]=='1':
            drawone(-400+60*int(i),-40)
        elif date[i]=='2':
            drawtwo(-400+60*int(i),-40)
        elif date[i]=='3':
            drawthree(-400+60*int(i),-40)
        elif date[i]=='4':
            drawfour(-400+60*int(i),-40)
        elif date[i]=='5':
            drawfive(-400+60*int(i),-40)
        elif date[i]=='6':
            drawsix(-400+60*int(i),-40)
        elif date[i]=='7':
            drawseven(-400+60*int(i),-40)
        elif date[i]=='8':
            draweight(-400+60*int(i),-40)
        elif date[i]=='9':
            drawnine(-400+60*int(i),-40)

STEP_LENGTH = 40    
t = turtle.Turtle()   
t.pensize(5)
main()
