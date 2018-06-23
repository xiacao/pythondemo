import turtle

def drawSnake(rad, angle, length, nackrad):
    for i in range(length):
        turtle.circle(rad, angle)
        turtle.circle(-rad, angle)
    turtle.circle(rad, angle/2)
    turtle.fd(rad)
    turtle.circle(nackrad+1, 180)
    turtle.fd(rad*2/3)

def main():
    turtle.setup(1300, 800, 0, 0)
    pythonsize = 30
    turtle.pensize(pythonsize)
    color = ['blue', 'red', 'green', 'purple']
    for x in range(1,7) :
        turtle.seth(-35)
        turtle.penup()
        turtle.goto(0.1*x, 0-100*x)
        turtle.pendown()
        turtle.pencolor(color[x%4])
        drawSnake(40, 70, 5, pythonsize/2)
        

main()
