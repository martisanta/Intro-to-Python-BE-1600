#sentinal loop
def print_average():
    s = 0
    count = 0
    values = 0 
    x = int(input("Type a number:"))
    if x < s:
        print("Average was 0")
    else:
        while x >= s:
            values += 1
            count += x
            x = int(input("Type a number:"))
        print("Average was ", (count / values))
print_average()
        
        
