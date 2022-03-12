
def function1(A,B):
    sum = 0
    for i in range (A,B):
        print(i, end= '')
        sum += i
    return sum
print(" Sum of integers is: ", function1(5, 11))
