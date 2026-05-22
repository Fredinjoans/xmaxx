#define a basic function
# def my_func():
#     print("Hello World")
#     name = input("What is your name? ")
#     print("Nice to meet you,",name)


# my_func()
# my_func(" How are you doing?") # this will cause an error because the function does not accept any parameters
# def cube(x):
#     return x**3

# result = cube(3)
# print(result)

# def my_func(greeting, name=None):
#     print("Hello World")
#     if name == None:
#         name = input("What is your name? ")
#     print(greeting, name)

# my_func("nice to meet you,", )
def multi_add(*args):
        result = 0
        for num in args:
            result += num
        return result

print(multi_add(10,1, 3, 4, 5))
