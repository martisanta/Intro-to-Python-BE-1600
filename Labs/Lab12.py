L =[[2, 3, 5],
    [-8, 4, 6],      
    [9, 3, 77],
    [11, -2, 9]]
print("2D list")
for r in range(len(L)):
    for c in range(len(L[r])):
        print("{0:2d}".format(L[r][c]), end= " ")
    print()
def function(L):
    L2 = []
    acc = 0
    for r in range(len(L)):
        for c in range(len(L[r])):
            if L[r][c] > 0 and L[r][c] % 2 == 0:
                acc += 1
        L2.append(acc)
        acc = 0
    print("Number of even non negative values")
    print("Row 1 :", L2[0])
    print("Row 2 :", L2[1])
    print("Row 3 :", L2[2])
    print("Row 4 :", L2[3])
    return L2
function(L)
