import calendar
c = calendar.TextCalendar(calendar.SUNDAY)
# thestr= c.formatmonth(2026, 1, 0, 0)
# print(thestr)
# hc = calendar.HTMLCalendar(calendar.SUNDAY)
# thestr= hc.formatmonth(2026, 1)
# print(thestr)
# for i in c.itermonthdays(2026, 8):
#     print(i)

for name in calendar.month_name:
    print(name)
for day in calendar.day_name:
    print(day)

print("team meetings will be on:")
for m in range (1,13):
    cal = calendar.monthcalendar(2026, m)
    week1= cal[0]
    week2 = cal[1]
    if week1[calendar.FRIDAY]!=0:
        meetday= week1[calendar.FRIDAY]
    else:
        meetday= week2[calendar.FRIDAY]
    print(f"{calendar.month_name[m]}: {meetday}")