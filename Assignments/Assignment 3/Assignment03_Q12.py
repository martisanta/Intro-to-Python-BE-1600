def function1():
    x = input("Enter a string")
    x = x.upper()
    x = list(x)
    d = {}
    for e in x:
        if e not in d:
            d[e] = 1
        else:
            d[e] += 1
    for i,j in d.items():
        j1 = "*" * j
        print(i,j1)

function1()
