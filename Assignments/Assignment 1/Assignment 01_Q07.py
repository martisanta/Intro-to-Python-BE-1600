import math
wallSpace = float(input("Enter wall space in square feet "))
price = float(input("Enter paint price per gallon "))
def function():
    gallon = math.ceil(float(wallSpace / 115))
    labor = math.ceil(float(gallon * 8))
    print("Gallons of paint: ", gallon)
    print("Hours of labor: ", labor)
    paintCharges = (float(price * gallon))
    laborCharges = (float(labor * 20))
    totalCost = (float(paintCharges + laborCharges))
    print("Paint charges:$", paintCharges)
    print("Labor charges:$", laborCharges)
    print("Total cost:$", totalCost)
function()
    
    
