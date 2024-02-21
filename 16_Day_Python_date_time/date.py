from datetime import datetime
now = datetime.now()
# print(dir(now))
day = now.day
month = now.month
year = now.year
hour= now.hour
minute= now.minute
second = now.second
timestamp  = now.timestamp()
# print(day,month, year, hour, minute, second,timestamp)

new_year = datetime(2025, 1,1,18,30,25 )
print(new_year)
day =  new_year.day
month = new_year.month
year = new_year.year
hour = new_year.hour
second= new_year.second
print(day,month,year,hour,minute,second)
now= datetime.now()
t = now.strftime("%H:%M:%S")
print(t)
time_one= now.strftime("%m/%d/%Y, %H:%M:%S %p")
print(time_one)
date_string = "5 December, 2019"
print("date_string = ", date_string)
date_object = datetime.strptime(date_string, "%d %B, %Y")
print("date_object = ",date_object)
from datetime import date
d = date(2020, 1, 1)
print(d)
print(d.today())
today= d.today()
