import turtle as tt
import time
tt.pensize(1)
tt.speed("fastest")
yp = 0
for x in range(100):
    tt.dot()
    tt.up()
    tt.setx(2 * x)
    tt.sety(yp % 255)
    tt.down()
    yp += 1;
    


