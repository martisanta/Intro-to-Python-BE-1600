import random
k = random.randint(2,9)
print(k)
L = []
print("Enter", k, "values")
for i in range(k):
    x1 = int(input("enter value"))
    L.append(x1)
print("Original List:", L)

def is_sorted(L):
    L1 = L[:]
    L1.sort()
    if L == L1:
        print("the list is sorted")
        return True
    else:
        print("the list is not sorted")
        return False 
is_sorted(L)
    
