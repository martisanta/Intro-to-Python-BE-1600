
L = input("Enter a string")
def double_list(L):
    L1 = []
    L = list(L.split())
    print("original list:", L)
    for e in L:
        for i in range (2):
            L1.append(e)
    print("double list:", L1)
    
    
double_list(L)
