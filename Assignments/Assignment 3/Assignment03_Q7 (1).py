strinG = input("Enter a string!")
strinG2 = strinG.upper()
L = list(strinG2)
d = {}
for e in L:
    if e not in d:
        d[e] = 1
    else:
        d[e] = d[e] + 1

v = list(d.values())
m = max(v)
for i in d.keys():
    if d[i] == m:
        print("The character that appears most frequently is ", i)
    
    
        

    
