#input
seconds = int(input("Total seconds is: "))

#variables
seconds_per_minute = 60
seconds_per_hour = 60 * 60
seconds_per_day = 24 * 60 * 60

#conversions
days = seconds // seconds_per_day
seconds = seconds % seconds_per_day

hours = seconds // seconds_per_hour
seconds = seconds % seconds_per_hour

minutes = seconds // seconds_per_minute
seconds = seconds % seconds_per_hour

#formatting using the %02d formatting, which converts all integers to two digits 
print("The converted result is: %d:%02d:%02d:%02d" % (days, hours, minutes, seconds))