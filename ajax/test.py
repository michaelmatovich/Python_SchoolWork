from datetime import date
from datetime import timedelta

today = date.today()

today_string = today.strftime("%Y-%m-%d")


print(today)

dates = ["2022-04-27","2022-04-26","2022-04-25","2022-04-24","2022-04-23","2022-04-22"]

print(dates)



new_date_string = today.strftime("%Y-%m-01")
print(new_date_string)



new_date = date(int(today.year), int(today.month), 1)

print(new_date.month)
print(new_date.year)
print(new_date.day)

new_date = new_date + timedelta(days = 31)
print(new_date)