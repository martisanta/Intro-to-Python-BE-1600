import math
def sphere_volume():
    r = float(input ("Enter the radius of a sphere: "))    
    print(r)
    volume = float (((4/3) * math.pi * r**3))
    print("Volume = ", volume)
sphere_volume()
