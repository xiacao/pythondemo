from graphics import *

face = Circle(Point(100,95),50)
 
leftEye = Circle(Point(80,80),5)
leftEye.setFill("Yellow")
leftEye.setOutline("Blue")
"""
rightEye = Circle(Point(120,80),5)
leftEye.setFill("Yellow")
leftEye.setOutline("Blue")
"""
rightEye = leftEye.clone()
rightEye.move(40,0)

mouth = Line(Point(80,110),Point(120,110))


win = GraphWin()
face.draw(win)
leftEye.draw(win)
rightEye.draw(win)
mouth.draw(win)
