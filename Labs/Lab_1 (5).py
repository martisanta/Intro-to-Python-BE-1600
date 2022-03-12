import math
x1 = float (input("Enter the first number "))
x2 = float (input("Enter the second number "))
x3 = float (input("Enter the third number "))
x4 = float (input("Enter the fourth number "))
x5 = float (input("Enter the fifth nunmber "))


def Avg():
    a = (x1 + x2 + x3 + x4 + x5)/5
    print ("Average = ", a)
    return a
def StandardDeviation(Avg):
    s = ((x1 - Avg)**2 + (x2 - Avg)**2 + (x3 - Avg)**2 + (x4 - Avg)**2 + (x5 - Avg)**2)/5
    print( "standard deviation = ", math.sqrt(s))
    
StandardDeviation(Avg())

    
