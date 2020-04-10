from math import pi
radius = float(input("The radius of the cylinder is: "))
height = float(input("The height of the cylinder is: "))
volume = round((radius ** 2) * pi * height, 1) 
print("The volume of the cylinder is " + str(volume) + " units.")
