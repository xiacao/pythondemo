from graphics import *

def insideRect(point, rect):
    locals()
    p1 = rect.getP1()
    p2 = rect.getP2()
    if p1.getX()>p2.getX():
        highX = p1.getX()
        lowX = p2.getX()
    else:
        highX = p2.getX()
        lowX = p1.getX()
    if p1.getY() > p2.getY():
        highY = p1.getY()
        lowY = p2.getY()
    else:
        highY = p2.getY()
        lowY = p1.getY()
    if point.getX()>=lowX and point.getX()<=highX and point.getY()>=lowY and point.getY()<=highY:
        return True
    return False

win = GraphWin("Celsius Converter", 400, 300)
win.setCoords(0.0, 0.0, 400.0, 300.0)#用这个坐标系映射原来的坐标系，即原来的坐标系会变成这个比例的坐标系还原要用x*scaleX,y*scaleY
# 绘制接口
Text(Point(120,230), " Celsius Temperature:").draw(win)
Text(Point(120,70), "Fahrenheit Temperature:").draw(win)
input = Entry(Point(280,230), 5)
input.setText("0.0")
input.draw(win)
output = Text(Point(280,70),"")
output.draw(win)
button = Text(Point(200,150),"Convert It")
button.draw(win)
rect = Rectangle(Point(100,100), Point(300,200))
rect.draw(win)
"""# 等待鼠标点击
win.getMouse()"""
point = win.getMouse()
while not insideRect(point, rect):
    point = win.getMouse()
# 转换输入
celsius = eval(input.getText())
fahrenheit = 9.0/5.0 * celsius + 32.0
# 显示输出，改变按钮
output.setText(fahrenheit)
button.setText("Quit")
# 等待响应鼠标点击，退出程序
#win.getMouse()
point = win.getMouse()
while not insideRect(point, rect):
    point = win.getMouse()
win.close()


