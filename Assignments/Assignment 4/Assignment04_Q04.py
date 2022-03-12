
x = input ("Enter file name")
f = open("words.txt", "r")
print("Letter    Count")
d ={ "a" : 0, "b": 0, "c": 0,"d": 0,"e": 0,"f": 0,"g": 0,"h": 0,"i": 0,
     "j": 0,"k": 0,"l": 0,"m": 0,"n": 0,"o": 0,"p": 0,"q": 0,"r": 0,
     "s": 0,"t": 0,"u": 0,"v": 0,"w": 0,"x": 0,"y": 0,"z": 0}

for line in f:
    line = line.lower()
    L = line.split()
    for word in L:
        word = list(word)
        for e in word:
            if e in d:
                value = int(d.get(e))
                value += 1
                d[e] = value

for j,k in d.items():
    print(j,"{0:7}".format(""),k)
    
    
    
    
    
