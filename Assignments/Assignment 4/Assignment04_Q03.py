f = open("thisFile.txt", "r")
x = open("thatFile.txt","w")
L2 = []
for line in f:
    strip = line.strip()
    L = strip.split("\n")
    L2.append(L)
for i in range(len(L2)):
    if i % 2 == 0:
        x.write("{}{}".format(str(L2[i]),"\n"))
     
f.close()
x.close()
