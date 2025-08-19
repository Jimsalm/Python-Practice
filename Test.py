import random

# a = 15
# if a > 10:
#     print('a is greater than 10')
# elif a == 10:
#     print('a is 10')
# else:
#     print('a is less than 10')


# fruits = ['apple', 'orange', 'watermelon']
# for x in fruits:
#     print(x)


# count = 1
# while count <= 5:
#     print("count: ", count)
#     count += 1

# for i in range(1,4):
#     print("\n")
#     for j in range(1,4):
#         print(f'i = {i}, j = {j}')

# for i in range(1,6):
#     if i == 3:
#         continue
#     print(i)

#
# a = 5
# b = 3
# c = a & b
# print(~b)

# my_list = [1,2,3,4,5,6,7,8,9]
# # my_list[0] = "orange"
# my_list.extend([10,11,12,13,14,15])
# print(my_list[:16])


"""
Prime numbers
"""

# divisors = [2,3,4,5,6,7,8,9,10]
# number = 100
# iterator = 2
#
# while iterator <= number:
#     for divisor in divisors:
#         if divisor == 10 and iterator % divisor != 0 and iterator != divisor:
#             print(iterator)
#             iterator += 1
#         elif iterator % divisor == 0 and iterator != divisor:
#             break
#     iterator += 1

"""
 palindrome checker 
"""

# word = input("Enter a word: ")
#
# word1 = word[::-1]
#
# if(word == word1):
#     print(word, "is a palindrome")
# else:
#     print(word, "is not a palindrome")


"""
Fibonacci Sequence 
"""

# counter = 0
# fiboStart = 0
# fiboEnd = 1
# counterMax = 12
# fibonacciSequence = []
# fiboNumber = 0
# fibonacciSequence.append(fiboStart)
# while counter < counterMax:
#     firstCounter = counter
#     secondCounter = counter - 1
#     if len(fibonacciSequence) >= 2:
#         fibonacciSequence.append(fibonacciSequence[firstCounter] + fibonacciSequence[secondCounter] )
#     else:
#         fibonacciSequence.append(fibonacciSequence[firstCounter] + fiboEnd)
#     counter += 1
# print(fibonacciSequence)


"""
Student Grade Calculator
"""

# assignments = []
# assignment_counter = 0
# while True:
#     try:
#        scores =  input("Enter your assignment scores: ")
#        if scores == 'd':
#            if len(assignments) < 1:
#                continue
#            else:
#                 break
#        else:
#         if int(scores) <= 70:
#                print("Score is too low")
#                continue
#         assignments.append(int(scores))
#     except ValueError:
#         print("Invalid input")
#
#
#
# total = assignments[0]
# for counter in range(1,len(assignments)):
#     total = total + assignments[counter]
#
# average = total/len(assignments)
# if 70 <= average <= 74:
#     letter_grade = "F"
# elif  75 <= average <= 79:
#     letter_grade = "C"
# elif 80 <= average <= 89:
#     letter_grade = "B"
# elif 90 <= average <= 100:
#     letter_grade = "A"
#
#
# print("Calculating final grade....")
# print('---------------------------')
# print(f'Total Assignments: {len(assignments)}')
# print(f'Average Score: {average:.2f}')
# print(f'Average Letter Grade: {letter_grade}')


"""
Odd or even
"""

# number = []
#
#
#
# while len(number) != 10:
#     try:
#         number.append(int(input("Enter a number: ")))
#     except ValueError:
#         print("Please enter a number")
#         continue
#
# def odd_even(number):
#     return "even"  if number % 2 == 0 else "odd"
#
# print(odd_even(num) for num in number)


"""
Square
"""
# numbers = [1,2,3,4,5]
#
# for number in range(len(numbers)):
#     numbers[number] = numbers[number]**2
#
# print(numbers)

"""
Password generator
"""
#
# lowercase_character = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
# uppercase_character = ['H', 'I', 'J', 'K', 'L', 'M', 'N']
# number_character = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
# symbol_character = ['!', '@', '#', '%', '$']
# all_character = [lowercase_character, uppercase_character, number_character, symbol_character]
# password = []
#
# wantedPassword = int(input('Enter your how many characters you wanted: '))
#
# counter =0
# while counter<=wantedPassword:
#     password.append(random.choice(random.choice(all_character)))
#     counter +=1
#
# print(password)
# for character in password:
#     print(character, end='')

"""
even numbers
"""
# list_of_number = []
# numbers = input("Enter number: ")
# separated_number = numbers.split(' ')
# for num in separated_number:
#     list_of_number.append(int(num))
#
# even = 0
# odd = 0
# for number in list_of_number:
#     if number % 2 == 0:
#         even += 1
#     else:
#         odd += 1
#
# print(even , odd)


"""
Grocery List
"""

print("Grocery List Manager \n ------------------------")
print("1. Add an Item")
print("2. Remove an Item")
print("3. View List")
print("4. Quit")

items = []

while True:
    choice = int(input("\nEnter your choice: "))
    match choice:
        case 1:
            item = input("Enter your item: ")
            items.append(item)
            continue
        case 2:
            item = input("Enter Item to remove: ")
            items.remove(item)
            if item not in items:
                print("Item not found")
                continue
        case 3:
          print("Your Items: ", end="")
          for i in items:
              print( i, end="  ")
          print()
        case 4:
            print("Goodbye")
            break
