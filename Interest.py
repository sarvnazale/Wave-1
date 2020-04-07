deposit = float(input("Your initial amount of deposit is: "))
year_one = deposit * 1.04
year_two = year_one * 1.04
year_three = year_two * 1.04
print("End of year one: " + str(round(year_one, 2)))
print("End of year two: " + str(round(year_two, 2)))
print("End of year three: " + str(round(year_three, 2)))