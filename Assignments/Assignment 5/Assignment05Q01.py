from cImage import*
import math
def Circle():
    myWin = ImageWin("circle", 400, 400)
    im = EmptyImage(600,400)
    for i in range(360):
        x = int(100 * math.cos(math.radians(i)))
        y = int(100 * math.sin(math.radians(i)))
        im.setPixel(200 + x,200 + y, Pixel(0, 0, 255))
    im.draw(myWin)
Circle()
