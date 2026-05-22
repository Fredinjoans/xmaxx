myint=10
myfloat=20.5
mystring="Hello, World!"
mybool=True
#print(myint)
#print(myfloat)
#print(mystring)
# print(mybool)
# print(myint+myfloat)
# print(myint*3)
# print(mystring*3)
# print(mybool and False)
# print(mybool or False)
# print(myint / myfloat)
# print(myint % 3)
# print(myint ** 2)  
# print(myfloat==10)
# print(myint>5 or myfloat<15)
string = [
    "Hello World!",
    "And how can this be? For he is the Kwisatz Haderach!",
    "Four score and seven years ago",
    "Life moves pretty fast. If you don’t stop and look around once in a while, you could miss it."
]
def find_largest(string):
    long = 0
    for l in string:
        if len(l)> long:
            long = len(l)      
    return long 
result = find_largest(string)
print(result)