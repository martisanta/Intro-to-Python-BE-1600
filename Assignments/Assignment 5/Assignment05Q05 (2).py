from cImage import *

def avg(firstPixel, secondPixel, thirdPixel,fourthPixel, fifthPixel):
    SumRed = firstPixel.getRed() + secondPixel.getRed()+\
    thirdPixel.getRed() + fourthPixel.getRed() + fifthPixel.getRed()
    SumGreen = firstPixel.getGreen() + secondPixel.getGreen()\
    + thirdPixel.getGreen() + fourthPixel.getGreen()+ fifthPixel.getGreen()
    SumBlue = firstPixel.getBlue() + secondPixel.getBlue() +\
    thirdPixel.getBlue() + fourthPixel.getBlue() + fifthPixel.getBlue()
    AvgRed = SumRed // 5
    AvgGreen = SumGreen //5
    AvgBlue = SumBlue // 5
    newPixel = Pixel(AvgRed, AvgGreen, AvgBlue)
    return newPixel
def smooth(imageFile):
    oldImage = FileImage(imageFile)
    width = oldImage.getWidth()
    height = oldImage.getHeight()

    myImageWindow = ImageWin("SmoothImage", width *2 , height)
    oldImage.draw(myImageWindow)
    newIm = EmptyImage(width, height)
    
    for row in range(1, height-2):
        for col in range(1,width-2):
            firstPixel = oldImage.getPixel(col, row)
            secondPixel = oldImage.getPixel((col - 1),row)
            thirdPixel = oldImage.getPixel((col + 1),row)
            fourthPixel = oldImage.getPixel(col, (row +1))
            fifthPixel = oldImage.getPixel(col, (row -1))
            newPixel = avg(firstPixel, secondPixel, thirdPixel,fourthPixel, fifthPixel)
            oldPixel = oldImage.getPixel(col, row)
            newIm.setPixel(col, row, newPixel)
    newIm.setPosition(width + 1, 0)
    newIm.draw(myImageWindow)
    myImageWindow.exitOnClick()

smooth("pic.gif")
            
    
    
    
