import datetime
today = datetime.date.today()
print(today)
print()

my_birthday = datetime.date(1994,4,8)
print(my_birthday)
print()

days_since_birth = today - my_birthday
print(days_since_birth)
print()
days_since_birth = (today - my_birthday).days
print(days_since_birth)
print()

print(today.year)
print(today.month)
print(today.day)
print(today.weekday())

