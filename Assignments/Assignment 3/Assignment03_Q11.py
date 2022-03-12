d1 = {"CS101" : 3004, "CS102": 4501, "CS103": 6755, "NT110": 1244, "CM241": 1411}
d2 = {"CS101": "Haynes", "CS102": "Alvarado", "CS103": "Rich", "NT110": "Burke", "CM241": "Lee"}
d3 = {"CS101": "8:00 am", "CS102": "9:00 am", "CS103": "10:00 am","NT110": "11:00 am", "CM241": "1:00 pm"}
x = input("Enter a course number")
if x not in d1:
    print( x, " is an invalid course number")
else:
    print("The details for the course ", x , "are:")
    print("Room:",d1.get(x))
    print("Instructor:", d2.get(x))
    print("Time:", d3.get(x))
        
