
import turtle
t = turtle.Turtle()
def drawsquare(i):
    x = 300
    for i in range (10):
        y = -x/2
        z = -x/2
        t.up()
        t.goto(y,z)
        t.down()
        
        for i in range (4):
            t.forward(x)
            t.left(90)
        x -= 10

drawsquare(t)
