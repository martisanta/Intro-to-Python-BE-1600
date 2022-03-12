
def function1():
    wA = int(input("Enter width"))
    lA = int(input("Enter length"))
    wB = int(input("Enter width"))
    lB = int(input("Enter length"))
    areaA = wA * lA
    areaB = wB * lB
    print("Area A: ", areaA)
    print("Area B: ", areaB)
    if areaA > areaB:
        print("Area A is greater than Area B")
    elif areaB > areaA:
        print("Area B is greater than Area A")
    else:
        print("Area A and Area B are equal")
    
function1()
