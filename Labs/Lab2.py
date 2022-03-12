
n = int(input("Enter a number: "))

def function1(n):
    for x in range (1, n +1):
        print(x, end =' ')

function1(n)
print("")

def function2(n):
    for x in range (n, 0, -1):
        print(x, end= ' ')
function2(n)


def function3(n):
    odds = 0
    for x in range (1, n + 1):
        if ((x % 2) != 0):
            odds += x
    print('')
    print("Sum of odd numbers:",odds)
function3(n)
def function4(n):
    evens = 0
    for x in range (1, n +1):
        if ((x % 2) == 0):
            evens += x
    print("Sum of even numbers:", evens)
function4(n)
