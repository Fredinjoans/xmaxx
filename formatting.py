from datetime import datetime
now = datetime.now()
# print(now.strftime("the current year is: %Y"))
# print(now.strftime("%a, %d %B, %y"))
# print(now.strftime("Local date and time: %c"))
# print(now.strftime("Local time: %X"))
# print(now.strftime("Local date: %x"))
print(now.strftime("current time: %I:%M:%S %p"))
print(now.strftime("current time: %H:%M"))