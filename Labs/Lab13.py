import random
x = random.randint(1,100)
print("I'm thinking of a number between 1 and 100...")
y = int(input("Your guess?"))
count = 1
while y != x:
    if y < x:
        print("It's higher")
        y = int(input("Your guess?"))
        count += 1
    if y > x:
        print("It's lower")
        y = int(input("Your guess?"))
        count += 1
print("You guessed it in", count, "guesses!")
