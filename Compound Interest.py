deposit = float(input("Your initial amount of deposit is: "))
interest = 1.04
year_one = deposit * interest
year_two = year_one * interest
year_three = year_two * interest
print("End of year one: " + "$" + str(round(year_one, 2)))
print("End of year two: " + "$" + str(round(year_two, 2)))
print("End of year three: " + "$" + str(round(year_three, 2)))
