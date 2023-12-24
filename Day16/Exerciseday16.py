#1. Get the current day, month, year, hour, minute and timestamp from datetime module

from datetime import datetime
now = datetime.now()
print(now)                      
day = now.day                   
month = now.month               
year = now.year                 
hour = now.hour                 
minute = now.minute             
timestamp = now.timestamp()
print(day, month, year, hour, minute)
print('timestamp', timestamp)
print(f'{day}/{month}/{year}, {hour}:{minute}')  


#2. Format the current date using this format: "%m/%d/%Y, %H:%M:%S")

from datetime import datetime
# current date and time
now = datetime.now()
t = now.strftime("%H:%M:%S")
print("time:", t)
time_one = now.strftime("%m/%d/%Y, %H:%M:%S")
# mm/dd/YY H:M:S format
print("time one:", time_one)


#3. Today is 5 December, 2019. Change this time string to time.

from datetime import datetime
date_string = "5 December, 2019"
print("date_string =", date_string)
date_object = datetime.strptime(date_string, "%d %B, %Y")
print("date_object =", date_object)


#4. Calculate the time difference between now and new year.

from datetime import datetime, timedelta

today = datetime(year=2023, month=12, day=20)
new_year = datetime(year=2024, month=1, day=1)
time_left_for_newyear = new_year - today
print('Time left for new year: ', time_left_for_newyear)

t1 = datetime(year=2023, month=12, day=20, hour=0, minute=59, second=0)
t2 = datetime(year=2024, month=1, day=1, hour=0, minute=0, second=0)
diff = t2 - t1
print('Time left for new year:', diff)


#5. from datetime import datetime

today = datetime(year=2023, month=12, day=20)
old_year = datetime(year=1970, month=1, day=1)
time_difference = today - old_year
print('Time difference between 1 January 1970 and now:', time_difference)

t1 = datetime(year=2023, month=12, day=20, hour=0, minute=59, second=0)
t2 = datetime(year=1970, month=1, day=1, hour=0, minute=0, second=0)
diff = t1 - t2
print('Time difference between 1 January 1970 and the specified date:', diff)


#6. 
# working with time zone e.g utc

from datetime import datetime, timezone, timedelta
utc_now = datetime.now(timezone.utc)
eastern_time = utc_now.astimezone(timezone(timedelta(hours=-5)))
print(f"UTC time: {utc_now}, Eastern Time: {eastern_time}")







