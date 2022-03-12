L = []
List_evens = []
List_odds = []
def function1(L):
    for i in range(10):
        x = int(input("enter a number"))
        L.append(x)
    print("List L: ", L)
    for i in range(len(L)):
        if L[i] % 2 == 0:
            List_evens.append(L[i])
        elif L[i] % 2 != 0:
            List_odds.append(L[i])
    print("Even numbers: ", List_evens)
    print("Odd numbers: ", List_odds)
            
function1(L)
    

    
    
