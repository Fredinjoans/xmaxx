from datetime import date
from datetime import datetime
from datetime import timedelta
# print(timedelta(days =365, hours =5, minutes= 1))
# now = datetime.now()
# print("Today is", now)
# print("In one year it will be:", now + timedelta(weeks=2, days=3))
# t = datetime.now() - timedelta(weeks=1)
# s = t.strftime("%A %B %d, %Y")
# print("One week ago it was ", s)
today= date.today()
today= date(today.year, 11, 10)
afd = date(today.year, 4, 1)
if afd< today:
    print(f"April fool'sday already went by {(today-afd).days} days ago")
    afd= afd.replace(year=today.year+1)
time_to_afd = afd-today
print(f"Its just {time_to_afd.days} days until april fool's days")