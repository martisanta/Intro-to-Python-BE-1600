
j = open("numbers.txt", "r")
count = 0; evens = 0; total = 0
dict = {}
for line in j:
    line1 = line.split()
    dict[line1[0]] = int(line1[1])
    count += 1
print("count:", count)
values = list(dict.values())
for i in values:
    total += i 
    if i % 2 == 0:
        evens += 1
print("sum:", total)
print("evens:", evens)
average = total / count
print("average: ", average )
    
        
        
    
