import random
even = 0
odd = 0
for i in range (100):
    x = random.randint(1,100)
    if ( x % 2) == 0:
        even += 1
    elif (x % 2) != 0:
        odd += 1

print("Out of 100 numbers, ", odd, " were odd and ", even, " were even.")
    
        
