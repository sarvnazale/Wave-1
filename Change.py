#getting user input
total_cent = int(input())

#defining variables
cents_per_toonie = 200
cents_per_loonie = 100
cents_per_quarter = 25
cents_per_dime = 10
cents_per_nickel = 5
cents_per_penny = 1

#calculating number of toonies
num_toonies = total_cent // cents_per_toonie
total_cent = total_cent % cents_per_toonie
print(num_toonies, "toonies")

#calculating number of loonies
num_loonies = total_cent // cents_per_loonie
total_cent = total_cent % cents_per_loonie
print(num_loonies, "loonies")

#calculating number of quarters
num_quarters = total_cent // cents_per_quarter
total_cent = total_cent % cents_per_quarter
print(num_quarters, "quarters")

#calculating number of dimes
num_dimes = total_cent // cents_per_dime
total_cent = total_cent % cents_per_dime
print(num_dimes, "dimes")

#calculating number of nickels
num_nickels = total_cent // cents_per_nickel
total_cent = total_cent % cents_per_nickel
print(num_nickels, "nickels")

#calculating number of pennies
print(total_cent, "cents" )