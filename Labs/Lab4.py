import random
n = random.randint(1,50)
print(n)
if n <= 2:
    print( "Package Weight: ", n)
    print( "Shipping rate: ",  "$", 1.10)
    print( "Shipping charge: ", "$", 1.10 * n)
elif 2 < n <= 6:
    print( "Package Weight: ", n)
    print( "Shipping rate: ",  "$", 2.20)
    print( "Shipping charge: ", "$", 2.20 * n)
elif 6 < n <= 10:
    print( "Package Weight: ", n)
    print( "Shipping rate: ",  "$", 3.70)
    print( "Shipping charge: ", "$", 3.70 * n)
elif 10 < n <= 20:
    print( "Package Weight: ", n)
    print( "Shipping rate: ",  "$", 4.50)
    print( "Shipping charge: ", "$", 4.50 * n)
elif n > 20:
    print("The package is over 20 pounds and cannot be shipped")
                    
                    
