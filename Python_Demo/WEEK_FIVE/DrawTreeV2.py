import turtle 




def drawtree(t,position,heading,length):
    if(length >= 4):
        t.up()
        t.setheading(heading)
        x,y = position
        t.setposition(x,y)
        t.down()
        t.forward(length)
        x,y = t.position()
        drawtree(t,(x,y),heading+65,3*length/5)
        drawtree(t,(x,y),heading-65,3*length/5)
             
def main():
    t = turtle.Turtle()
    t.pencolor("green")
    t.pensize(5)
    t.setheading(90)
    t.speed(10)
    t.penup()
    t.sety(-250)
    t.pendown()
    turtle.tracer(False)
    drawtree(t,t.position(),t.heading(),300)
    turtle.tracer(True)
    
    
    
main()
