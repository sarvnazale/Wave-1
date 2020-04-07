length = float(input("The length of the field in feet is: "))
width = float(input("The width of the field in feet is: "))
Area = round(length * width / 43560, 2)
print("The area of the field is " + str(Area) + " acres.")