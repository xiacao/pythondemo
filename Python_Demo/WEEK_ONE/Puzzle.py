import turtle as tt
import time
tt.pensize(2)
tt.speed("fastest")
tt.begin_fill()
for x in range(100):
    tt.forward(2*x)
    tt.left(90)

tt.end_fill()
