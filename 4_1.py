#python date

#1 Write a Python program to subtract five days from current date.
import datetime

from datetime import timedelta, datetime
x = datetime.now()
fivedago = x - timedelta(days = 5)
print("5 days ago was:", fivedago.strftime("%Y-%m-%d"))

#2 Write a Python program to print yesterday, today, tomorrow.
x = datetime.now()
delta = timedelta(days = 1)
print("yesterday:", (x - delta).strftime("%Y-%m-%d"), "today:", x.strftime("%Y-%m-%d"), "tomorrow:", (x + delta).strftime("%Y-%m-%d"))

#3 Write a Python program to drop microseconds from datetime.
x = datetime.now()
y = x.replace(microsecond=0)
print("Current Datetime:", x)
print("Datetime without microseconds:", y)

#4 Write a Python program to calculate two date difference in seconds.
date1 = datetime(2025, 2, 5, 14, 30, 0)
date2 = datetime(2025, 2, 3, 12, 15, 0)

difference = (date1 - date2).total_seconds()
print("Difference in seconds:", difference, "seconds")

