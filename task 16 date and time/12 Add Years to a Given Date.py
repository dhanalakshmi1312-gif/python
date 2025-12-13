import datetime

def addYears(d, years):
    try:
        return d.replace(year=d.year + years)
    except ValueError:
        return d.replace(month=2, day=28, year=d.year + years)

print(addYears(datetime.date(2015,1,1), -1))
print(addYears(datetime.date(2015,1,1), 3))
print(addYears(datetime.date(2015,1,1), 2))
print(addYears(datetime.date(2000,2,29), 1))
