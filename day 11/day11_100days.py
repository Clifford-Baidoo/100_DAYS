#Seconds in a year
# 1 year = 365 days
# 1 day = 60 minutes
# 1 minitue = 60 seconds 

years = int(input("How many years do you want to calclulate for > "))
leap_year = input("Is it a leap year > ")

days = years * 365
if leap_year == "yes":
    days = days + 1 
hours = ( days * 24 )
minutes = hours * 60
seconds = minutes * 60

print("There are ", seconds , "seconds in", years, "year(S)")