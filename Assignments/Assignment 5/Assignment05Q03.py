      
from cImage import *
global x, y
x = int(input("enter x"))
y = int(input("enter y")) 
def dimensions(oldImage):
    global x, y
    oldW = oldImage.getWidth()
    oldH = oldImage.getHeight()

    newIm = EmptyImage(oldW * x, oldH * y)

    for row in range(newIm.getHeight()):
        for col in range(newIm.getWidth()):

            originalCol = col // x
            originalRow = row // y
            oldPixel = oldImage.getPixel(originalCol, originalRow)

            newIm.setPixel(col, row, oldPixel)

    return newIm

def makeImage(imageFile):
    oldImage = FileImage(imageFile)
    width = oldImage.getWidth()
    height = oldImage.getHeight()
    
    myWin = ImageWin("New Image", width * x, height * (y))
    
    newImage = dimensions(oldImage)
    newImage.draw(myWin)

    myWin.exitOnClick()

makeImage("butterfly.gif")    
