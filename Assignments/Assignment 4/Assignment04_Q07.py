import random
def dice_sum():
    x = int(input("Desired dice sum:"))
    y = random.randint(1,6)
    z = random.randint(1,6)
    sum = y + z
    print(y, "and", z , "=", sum)
    while sum != x:
        y = random.randint(1,6)
        z = random.randint(1,6)
        sum = y + z
        print(y, "and", z , "=", sum)
dice_sum()
        
        
