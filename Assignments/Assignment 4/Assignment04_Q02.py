##Write a program that writes a temperature conversion table called tempconv. 
##txt. The table should include temperatures from -10 to 10 degrees Fahrenheit
##and their Celsius equivalents, presented in two columns with appropriate
##headings. Each column should be 12 characters wide, and each temperature
##should have 2 digits to the right of the decimal point.

import csv
f = open("tempconv.txt", "w")
f.write("{0:12s}{1:12s}".format("Fahrenheit", "Celsius"))
f.write("\n")
far = float(-10.00)
for x in range(21):
    cel = float((far - 32)*(5/9))
    f.write("{0:<12.2f}{1:<12.2f}".format(far,cel))
    far += 1
    f.write("\n")
f.close()
