# Get the current day, month, year, hour, minute and timestamp from datetime module
from datetime import datetime, date, timedelta

today = datetime.now()
day = today.day
month = today.month
year = today.year
hour = today.hour
minute = today.minute
timestamp = today.timestamp()

print(f'{day}/{month}/{year} - {hour}:{minute} A:M - timestamp: {timestamp}')


# Format the current date using this format: "%m/%d/%Y, %H:%M:%S")
print(today.strftime("%m/%d/%Y, %H:%M:%S"))


# Today is 5 December, 2019. Change this time string to time.
today_str = "5 December, 2019"
today_str_to_time = datetime.strptime(today_str, "%d %B, %Y")

print(today_str_to_time)


# Calculate the time difference between now and new year.
date1 = date(year=2026, month=3, day=6)
new_year = date(year=2027, month=1, day=1)
difference_time = new_year - date1

print(f'For new year we have left: {difference_time}')


# Calculate the time difference between 1 January 1970 and now.
unix = date(year=1970, month=1, day=1)
this_date = date(year=2026, month=3, day=6)
difference_unix = this_date - unix

print(f'I\'ts been this amount of time: {difference_unix}')



