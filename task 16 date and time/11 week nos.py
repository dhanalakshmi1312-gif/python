import datetime

date = datetime.date(2015, 6, 16)
week_number = date.strftime("%U")

print("Week Number:", week_number)
