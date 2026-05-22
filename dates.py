from datetime import date
from datetime import datetime
today = date.today()
print("Today's date is",today)
print("Date Components",today.day, today.month, today.year)
print("Today's Weekday", today.weekday())
days = ["mon","tue", "wed", "thu", "fri", "sat","sun"]
print("which is a", days[today.weekday()])
t = datetime.now()
print("the current date and time is", t)