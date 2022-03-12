import math
f = open("data.txt", "r")
line =f.readlines()
L = [[float(i.split()[0]), float(i.split()[1])] for i in f]
d = []
for i in L:
    coordinate = []
    for j in L:
        distance = round(math.sqrt( ((i[0] - j[0]**2) + ((i[1] -j[1]) **2)), 2))
        table = "{0:6s}".format(str(distance))
        coordinate.append(table)
        d.append(coordinate)
d.insert(0, ['      P1','     P2', '     P3', '     P4', '     P5','     P6', '     P7', '     P8'])
for i in range(len(d)):
    num = i
    if num == 0:
        print("0")
    else:
        print("P{0:6s}". format(str(num)), end= "")
    for j in range(len(d[i])):
        print(d[i][j], end = "")
    print('')

