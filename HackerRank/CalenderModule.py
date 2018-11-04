# import calendar
# print(calendar.TextCalendar(firstweekday=5).formatyear(2018))

import calendar
date = input().split(" ")

day=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
#print(calendar.weekday(int(date[2]),int(date[1]),int(date[0])))

YEAR =int(date[2].strip())
MONTH =int(date[0].strip())
DAY =int(date[1].strip())


print(day[calendar.weekday(YEAR,MONTH,DAY)].upper())