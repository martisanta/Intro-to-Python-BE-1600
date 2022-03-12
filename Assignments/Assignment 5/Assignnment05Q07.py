L = [[0,0,0],
     [0,0,0],
     [0,0,0],
     [0,0,0]]
print("part a")
for r in range(len(L)):
    for c in range(len(L[r])):
        print(L[r][c], end= "")
    print()
print("part b")
for r in range(len(L)):
    for c in range(len(L[r])):
        n = 0
        for i in range(3):
            L[0][n] = 1
            n += 1
        n = 0
        for i in range(3):
            L[1][n] = 3
            n+= 1
        n = 0
        for i in range(3):
            L[2][n] = 3
            n += 1
        n = 0
        for i in range(3):
            L[3][n] = 3
            n += 1
        print(L[r][c], end= "")
    print()
print("part c")
for r in range(len(L)):
    for c in range(len(L[r])):
        n = 0
        for i in range(4):
            L[n][0] = 2
            n += 1
        n = 0
        for i in range(4):
            L[n][1] = 2 * L[0][0]
            n += 1
        n = 0
        for i in range(4):
            L[n][2] = 2 * L[1][1]
            n += 1
        print(L[r][c], end = "")
    print()
        
