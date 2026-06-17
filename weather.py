city = input("Enter the name of your city :")
temp = float(input("Enter today's temeprature in C:"))
if temp > 35:
    print("Warning : It is very hot today! ")
if temp > 25:
    print("Great day to go outside!")
else:
    print("Grab a jacket it is cold!")
if temp > 35:
    print("Weather : Scorching hot!")
elif temp > 25:
    print("Weather : Warm and sunny!")
elif temp > 15:
    print("Weather : Cool and breezy!")
else:
    print("Stay warm !")
import datetime
import calendar
now = datetime.datetime.now()
print("City:",city)
print("Time now:",now)

print(calendar.calendar(now.year))