import random
count = 0
flip = 0
print("Enter 1 for Head")
print("Enter 2 for Tail")
z = int(input("Enter 9 to exit\n"))
while z != 9:
    f = random.randint(1,2)
    flip += 1
    if z == f:
        count += 1
        print("You won!")
    else:
        print("You lost!")
    print("Enter 1 for Head")
    print("Enter 2 for Tail")
    z = int(input("Enter 9 to exit\n"))
print("Number of flips:", flip)
print("You won", count, "time(s)")
    

