import datetime

# 1 current date and time
now = datetime.datetime.now()
print("Current:", now)


# 2 difference between two dates
date1 = datetime.date(2024, 1, 1)
date2 = datetime.date(2024, 12, 31)
difference = (date2 - date1).days
print("Days difference:", difference)


# 3 add 7 days
today = datetime.date.today()
new_date = today + datetime.timedelta(days=7)
print("After 7 days:", new_date)


# 4 format date
formatted = now.strftime("%Y-%m-%d")
print("Formatted:", formatted)


# 5 get weekday
weekday = today.weekday()  # Monday=0
print("Weekday number:", weekday)