import math
radius = int(input("Enter a radius"))
x = int(input("Enter x coordinate value"))
y = int(input("Enter y coordinate value"))
point = [x, y]
d = math.sqrt((x**2 + y **2)) 
def inCircle(point, radius):
    if d <= radius:
        print(point, "is in circle with radius ", radius)
    elif d > radius:
        print(point, "is not in circle with radius ", radius)
inCircle(point, radius)
        
    
