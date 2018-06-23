import turtle
turtle.pensize(2)
turtle.bgcolor("black")
colors = ["red", "yellow", "purple", "blue"]
turtle.speed("fastest")
for x in range(400):
    turtle.forward(2 * x)
    turtle.left(91)
    turtle.color(colors[x % 4])

