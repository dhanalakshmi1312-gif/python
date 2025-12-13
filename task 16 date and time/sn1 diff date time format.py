import datetime

now = datetime.datetime.now()
t = now.timetuple()

print("a) Current date and time:", now)
print("b) Current year:", now.year)
print("c) Month of year:", now.month)
print("d) Week number of the year:", now.strftime("%U"))
print("e) Weekday of the week:", now.strftime("%A"))
print("f) Day of year:", t.tm_yday)
print("g) Day of the month:", now.day)
print("h) Day of week:", t.tm_wday)
