x = int(input("Enter a number"))
y = int(input("Enter another number"))
sum = float(x + y)
print("The sum of the numbers you entered is", sum)
a = input("Do you want to do that again? (y/n)")
while a == "y":
    x = int(input("Enter a number"))
    y = int(input("Enter another number"))
    sum = float(x + y)
    print("The sum of the numbers you entered is", sum)
    a = input("Do you want to do that again? (y/n)")
