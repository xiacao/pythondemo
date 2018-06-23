from graphics import *
 
p1 = Point(100, 100)
print(p1.getX())
p2 = Point(150,80)
win = GraphWin("you know",600,300)
win.setCoords(0.0, 0.0, 600.0, 300.0)#本来坐标系是在(0, 0)点现在更改之后在(0,300)点而且Y轴方向改变
#p1.move(50,-20)#移动
print(p1.getX(), p1.getY())
p1.draw(win)
p2.draw(win)

