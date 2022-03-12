L = []
def getData(L):
    print("Enter highest temperatures for each month of the year")
    for r in range(2):
        temp = []
        for c in range(12):
            print("Month", c+1, ":", end ="")
            x = int(input())
            temp.append(x)
        L.append(temp)
        print("Enter lowest temperatures for each month of the year")
    return L
def averageHigh():
    for r in range(len(L)):
        acc = 0
        for c in range(len(L[r])):
            acc = acc + L[0][c]
        avg = acc / 12 
    return avg

def averageLow():
    for r in range(len(L)):
        acc = 0
        for c in range(len(L[r])):
            acc = acc + L[1][c]
        avg = acc / 12
    return avg

def highTemp():
    L2 = []
    for r in range(len(L)):
        for c in range(len(L[r])):
            L2.append(L[0][c])
            highest = max(L2)
    return highest
def lowTemp():
    L2 = []
    for r in range(len(L)):
        for c in range(len(L[r])):
            L2.append(L[1][c])
            lowest = min(L2)
    return lowest
getData(L)
highave = averageHigh()
lowave = averageLow()
highest = highTemp()
lowest = lowTemp()
print("List of highest and lowest temperatures for each month of the year")
for r in range(len(L)):
    for c in range(len(L[r])):
        print(L[r][c], " ", end= "")
    print()
print(" ")
print("Average high temperature for the year", highave)
print("Average low temperature for the year", lowave)
print("Highest high temperature for the year", highest)
print("Lowest low temperature for the year", lowest)
