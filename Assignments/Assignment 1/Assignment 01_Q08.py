
def function(x1,x2):
    acc = 0
    for x in range(x1, x2+10, 10):
        print(acc, end = ' ')
        acc += 10
        
function(0, 100)
