from graphics import *

def convert(inputPart):
    celsius = eval(inputPart.getText())#输入转换
    fahrenheit = 9.0/5.0 * celsius + 32
    return fahrenheit

def colorChange(win, inputPart):
    cnum = eval(inputPart.getText())
    weight = cnum / 100.0
    newcolor = color_rgb(int(255*weight), int(66+150*(1-weight)), int(255*(1-weight)))
    win.setBackground(newcolor)

def main():
    win = GraphWin("Celsius Converter", 400, 300)
    win.setCoords(0.0, 0.0, 3.0, 4.0)
    #绘制输入接口
    Text(Point(1,3), " Celsius Temoerature:").draw(win)
    Text(Point(2,2.7), " (Please input 0.0-100.0 )").draw(win)
    Text(Point(1,1), "Fahrenheit Temperature:").draw(win)
    inputPart = Entry(Point(2,3), 5)
    inputPart.setText("0.0")
    inputPart.draw(win)
    output = Text(Point(2, 1), "")
    output.draw(win)
    button = Text(Point(1.5, 2.0), "Convert It")
    button.draw(win)
    rect = Rectangle(Point(1, 1.5), Point(2, 2.5))
    rect.draw(win)
    win.getMouse()
    result = convert(inputPart)
    output.setText(result)
    colorChange(win, inputPart)
    button.setText("Quit")
    win.getMouse()
    win.close()

if __name__ == '__main__':
    main()

