Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 22:45:29) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import calendar
import daytime
import time

print(calendar.weekheader(6))
print()

print(calendar.firstweekday())
print()

print(calendar.month(2020, 3))
print()

print(calendar.calendar(2020))


print(calendar.weekday(2020, 3, 8))

day_of_the_week = calendar.weekday(2020, 2, 22)
print(day_of_the_week)

# year 2030
print(calendar.weekday(2030, 3, 8))

# year 2080
print(calendar.weekday(2080, 3, 8))


# year 3000
print(calendar.weekday(3000, 3, 8))


# year 4900
print(calendar.weekday(4900, 3, 8))

# leap
is_leap = calendar.isleap(2020)
print(is_leap)

print(calendar.isleap(2021))

how_many_leap_days = calendar.leapdays(2020, 2024)
print(how_many_leap_days)

print(calendar.leapdays(2020, 2028))

