def function_1():
    L = []
    acc = 0
    for i in range(10):
        x = int(input('Enter a number'))
        L.append(x)
    for e in L:
        acc += e
            
    print(L)
    minimum = min(L)
    maximum = max(L)
    avg = (acc / 10)
    print ("Low: ", minimum)
    print("High: ", maximum)
    print("Total: ", acc)
    print("Average: ", avg)
function_1()
