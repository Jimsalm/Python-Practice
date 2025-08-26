# Variables
# variableName = value

# a = 5  # int
# print(type(a))
# a = "Hello"  # str
# print(type(a))
# a = 3.14  # float
# print(type(a))
# a = True  # bool
# print(type(a))

# Collections
# # list
# lst = [1]
# print(type(lst))
# print(len(lst))
# # tuple
# tup = 1, 2, 3, 4
# print(type(tup))
# print(len(tup))
# # set
# st = {1, 2, 3, 4}
# print(type(st))
# # dict
# dct = {"one": 1, "two": 2}
# print(type(dct))

# Input (input()) and Output (print())
# name = input("Enter name: ")
# print("Name: " + name)
# age = int(input("Enter age: "))
# # print("Age: " + age)
# print(f"Age: {age}")  # f-strings

# amount = float(input("Enter amount: "))
# print(f"Amount: {amount:,.2f}")
# 1,000.00

# if statement
# x = 20
# if x == 19:
#     print(f'{x} is equal to 19.')
# elif x > 19:
#     print(f'{x} is greater than 19.')
    # if x % 2 == 0:  # even
    #     print(f'{x} is even.')
    # else:
    #     print(f'{x} is odd.')
    # print(f'{x} is even.') if x % 2 == 0 else print(f'{x} is odd.')
    # print(f'{x} is even.' if x % 2 == 0 else f'{x} is odd.')
    # a = f'{x} is even.' if x % 2 == 0 else f'{x} is odd.'
    # print(a)

    # Ternary operation
    # Other language - Ternary operator - ?
    # condition ? true : false;
    # True if condition else False
# else:
#     print(f'{x} is less than 19.')

# For Loop - Sequences
# sequences - collections, string, range()

# range(stop)
# for i in range(10):
#     print(i, end=" ")
# 0 1 2 3 4 5 6 7 8 9

# range(start, stop)
# for i in range(2, 11, 2):
#     print(i, end=" ")

# [print(f'{x} is even.' if x % 2 == 0 else f'{x} is odd.') for x in range(1, 11)]
# Shorthand for loop
# [statement for var in sequence]
# 1 2 3 4 5 6 7 8 9 10

# range(start, stop, step)
# for i in range(10, 0, -1):
#     print(i, end=" ")
# 10 9 8 7 6 5 4 3 2 1

# While Loop - Conditions
# while 0:
#     pass
# else:
#     print('terminated!')

# Lists
names = ['Renz Carlos', 'Brix', 'Christian', 'James', 'Christian', 'Oliver']
print(len(names) + names.count('Christian'))

