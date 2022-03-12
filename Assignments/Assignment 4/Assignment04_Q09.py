import random
def three_heads():
    y = 1
    L = []
    i = 0
    while y == 1:
        x = random.randint(0,1)
        if x == 1:
            print("H", end = "")
            L.append("H")
            
        if x == 0:
            print("T", end = "")
            L.append("T")
            
        if i >= 2:
            if L[i-2]=='H' and L[i-1]=='H' and L[i]=='H':
                y = 0
                print("\n", "Three Heads in a row!")
        i += 1      
three_heads()

