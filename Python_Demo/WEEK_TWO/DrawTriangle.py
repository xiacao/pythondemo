import turtle

def drawTriangle(length):
    turtle.color("red")
    turtle.begin_fill()
    turtle.seth(0)
    turtle.forward(length)
    turtle.seth(120)
    turtle.forward(length)
    turtle.seth(240)
    turtle.forward(length)
    turtle.end_fill()

        

drawTriangle(200)
