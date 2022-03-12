
L = input("Enter a string")
L1 = []
def remove_duplicates(L):
    d = {}
    L = list(L.split())
    print("original list:", L)
    for e in L:
        if e not in L1:
            L1.append(e)
    print("list after removing duplicates",L1)
        
remove_duplicates(L)
        
