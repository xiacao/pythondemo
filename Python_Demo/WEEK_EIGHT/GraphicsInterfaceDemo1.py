from graphics import *

def main():
    win = GraphWin("Click Me!")
    for i in range(10):
        p = win.getMouse()
        print("You Clicked at:", p.getX(), p.getY())

if __name__ == '__main__':
    main()
