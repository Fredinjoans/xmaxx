x=0
while x < 10:
    #rint(x)
    x += 1
# answer = input('should we continue? (yes/no) ')
# while answer == 'yes':
#     print("Continuing...")
#     answer = input('should we continue? (yes/no) ')

# for loop
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
# for d in days:

#     print(d)

#use break to exit the loop when a condition is met
# for d in days:
#     if d == "Wednesday":
#         break
#     print(d)

# for d in days:
#     if d == "Wednesday":
#         continue
#     print(d)

for i, d in enumerate(days):
    print(i,d)