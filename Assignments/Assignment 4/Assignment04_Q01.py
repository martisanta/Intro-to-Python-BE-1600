##Write a program that writes a series of random numbers to a file. Each random 
##number should be in the range of 1 through 100. The application should let the user 
##specify the file name and how many random numbers the file will hold.
import random
import csv
x = input("Enter the name of the file to which results should be written:")
y = int(input("Enter the number of random numbers to be written to the file:"))
randomfile = open(x ,"w")
for i in range(y):
    line = str(random.randint(1,100))
    randomfile.write(line)
    randomfile.write("\n")
    print(line)
randomfile.close()
