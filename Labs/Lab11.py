from cImage import*

myImWin = ImageWin("Line Image", 300, 300)
lineImage = EmptyImage(300,300)
redPixel = Pixel(255, 0,0)
bluePixel = Pixel(0,0,255)
for i in range(150, 300):
    lineImage.setPixel(150, i, redPixel)
for i in range(300):
    lineImage.setPixel(i,i, bluePixel)
    lineImage.setPixel(299-i, i, bluePixel)
lineImage.setPixel(i,i, redPixel)


lineImage.draw(myImWin)
lineImage.save("lineImage.gif")
myImWin.exitOnClick()

