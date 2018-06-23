import turtle as tt
import time
tt.pensize(1)
tt.speed("fastest")
yp = 0
for i in range(5):
    tt.speed(i*2)
    for x in range(i*100,i*100+100):
        tt.dot()
        tt.up()
        tt.setx(-500 + 2 * x)
        tt.sety(yp)
        tt.down()
        if yp == 0:
            yp = 255
        else :
            yp = 0
    


