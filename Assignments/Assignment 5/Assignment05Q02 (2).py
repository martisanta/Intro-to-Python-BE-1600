      
from cImage import *

def redIntensity(oldPixel):
    oldGreen = oldPixel.getGreen()
    oldBlue = oldPixel.getBlue()
    if oldPixel.getRed() < 180:
        newRed = oldPixel.getRed() + 100
    else:
        newRed = oldPixel.getRed()
    newPixel = Pixel(newRed, oldGreen, oldBlue)
    return newPixel
    

def makeRed(imageFile):
    oldImage = FileImage(imageFile)
    width = oldImage.getWidth()
    height = oldImage.getHeight()

    myImageWindow = ImageWin("NewImage", width * 2, height)
    oldImage.draw(myImageWindow)
    newIm = EmptyImage(width, height)

    for row in range(height):
        for col in range(width):
            oldPixel = oldImage.getPixel(col,row)							
            newPixel = redIntensity(oldPixel)							
            newIm.setPixel(col, row, newPixel)

    newIm.setPosition(width + 1, 0)
    newIm.draw(myImageWindow)
    myImageWindow.exitOnClick()

makeRed("butterfly.gif")
