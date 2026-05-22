mydict = { 
    "one": 1,
    "two": 2,
    3: "three",
    4.5: "four point five",
    True: "boolean true" 
}
# print(mydict)
# print(mydict["one"])
# print(mydict[3])
# print(mydict[4.5])
# print(mydict[True])
# mydict["five"] = 5
# print(mydict)
# mydict["seven"] = 7
print(mydict)
print("two" in mydict)
print( 2 in mydict)
print(mydict.keys())
print(mydict.values())
for key,value in mydict.items():
    print(key, value)
    