print("First nested loop")
num = 7
for i in range(1,7+1):
    for k in range(1, i+ 1):
        print("* " , end= "")
    print()
print("Second nested loop")
for i in range(7):
    for k in range(i, 7):
        print("* ", end= "")
    print()
    
    
