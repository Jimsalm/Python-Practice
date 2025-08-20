###Problem #1


# height_input = int(input("Height: "))
# char_input = input("Character input: ")
#
# print(char_input * 12)
#
# for i in range(1, height_input - 1):
#     print(char_input + (" " * 10) + char_input )
#
# print(char_input * 12)


#Problem #2 Pyramid number

# user_input = int(input("User input: "))
# number_counter = 1
#
# for i in range(user_input):
#     if user_input <= number_counter:
#         break
#     for j in range(i):
#         # print(f'{j} j counter')
#         print(number_counter, end="")
#         number_counter += 1
#         if user_input < number_counter:
#             break
#     print()







#Problem #4 Pyramid number

# user_input = int(input("User input: "))
# height_counter = 0
# number_counter = 1
#
# for i in range(user_input):
#     if user_input < number_counter:
#         break
#     for j in range(i):
#         number_counter += 1
#         if user_input < number_counter:
#             break
#         height_counter += j
#
# print(height_counter)








#Problem #5

user_input = int(input("Please enter a number: "))
total_sum = 0


while True:

    if user_input == 0:
        user_input = int(input("Please enter greater 0: "))

    else:
        for i in range(1, user_input):
            total_sum += i ** 3
        print(f'The sum of all cubes is {total_sum}.')
        break















