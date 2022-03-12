speed = int(input("Enter the speed of the vehicle in mph: "))
hours = int(input("Enter the number of hours traveled: "))

def function1(speed, hours):
    print("Hour        Distance Traveled")
    print("-----------------------------")
    total = 0
    for i in range(1, hours+1):
        print(i, "         ", i * speed)
        distance = i * speed
        total += distance 
    print("The accumalated distance traveled is: ", total)
   

    
         
        
function1(speed, hours)
