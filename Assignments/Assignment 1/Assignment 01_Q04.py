kiloMeters = float (input("Enter the distance in kilometers: "))

def conversion(kiloMeters):
  print("The distance in kilometers is ", kiloMeters)
  miles = float(kiloMeters * 0.6214)
  print("The conversion of ", kiloMeters, " kilometers to miles is ", miles," miles.")

conversion(kiloMeters)    
    
