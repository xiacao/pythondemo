from graphics import *

win = GraphWin("Draw a polygon", 300, 300)
win.setCoords(0.0, 0.0, 300.0, 300.0)
message = Text(Point(150, 20),"Click on five points")
message.draw(win)
#获得鼠标点击的五个点
p1 = win.getMouse()
p1.draw(win)
p2 = win.getMouse()
p2.draw(win)
p3 = win.getMouse()
p3.draw(win)
p4 = win.getMouse()
p4.draw(win)
p5 = win.getMouse()
p5.draw(win)
#使用Polygon对象绘制多边形
polygon = Polygon(p1, p2, p3, p4, p5)
polygon.setFill("peachpuff")
polygon.setOutline("blue")
polygon.draw(win)
#等待响应鼠标事件，退出程序
message.setText("Click anywhere to quit.")
win.getMouse()
