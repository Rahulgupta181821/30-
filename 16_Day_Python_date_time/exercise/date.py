from datetime import datetime
d = datetime.now()
print(d)
year = d.year
day= d.day
month= d.month
hour= d.hour
minute = d.minute
second= d.second
timestamp = d.timestamp()
print(day,month,year,hour,minute,second,timestamp)
print(year)
today = d.today()
date_time = datetime.strftime(today,'%m/%d/%Y, %H:%M:%S %p')
print(date_time)
from datetime import date
date_string = '5-December, 2019'
date_time = datetime.strptime(date_string, '%d-%B, %Y')
print(date_time)
# print(today)
today = date(year=2024, month=2, day=21)
new_year = date(year= 2025, month=1, day=1)
time_left_for_newyear = new_year -today
print(time_left_for_newyear)
previous_year = date(year=1970, month=1, day=1)
time_diff = today - previous_year
print(time_diff)