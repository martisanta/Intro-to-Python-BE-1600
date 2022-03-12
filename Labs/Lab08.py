
d= {'Kendrick': 'Perkins', 'Stuart': 'Reges', 'Jessica': 'Wolk', 
 'Bruce': 'Reges', 'Hal': 'Perkins'}
def is_unique(d):
    d2 = {}
    for e in d.values():
        if e not in d2:
            d2[e] = 1
        else:
            d2[e] = d2[e] + 1
    if d2[e] > 1:
        return False
    else:
        return True
print(is_unique(d))
