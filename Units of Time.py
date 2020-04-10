#input
days = int(input("Enter the number of days: "))
hours = int(input("Enter the number of hours: "))
minutes = int(input("Enter the number of minutes: "))
seconds = int(input("Enter the number of seconds: "))

#variables
seconds_per_minute = 60
seconds_per_hour = 60 * 60
seconds_per_day = 24 * 60 * 60

#conversions
total_in_seconds = (days * seconds_per_day) + (hours * seconds_per_hour) + (minutes * seconds_per_minute) + seconds

print("The total in seconds is:", total_in_seconds)