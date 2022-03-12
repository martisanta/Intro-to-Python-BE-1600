x = int(input("Enter the number of years:"))
yearcounter = 1
for i in range(x):
    acc = 0
    counter = 0
    print("For year", yearcounter )
    yearcounter += 1
    for j in range(12):
        print("Enter the rainfaill amount for the month", j+1, ":", end = "")
        y = float(input())
        acc += y
        counter += 1
    avg = acc / counter
print("For", x * 12,"months")
print("Total rainfall:", acc)
print("Average monthly rainfall:", avg)
        
