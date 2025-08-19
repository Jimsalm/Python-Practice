
# number = [1, 2, 3, 4, 5]
# square_number  = []

# for i in range(len(number)):
#     square_number.append(number[i] ** 2)
#     print(square_number[i])
    
    
# number = [10, 23, 45, 58, 77, 90]

# for i in range(len(number)):
#     if number[i] % 2 == 0:
#         print(number[i])

# numbers = [12, 7, 9, 24, 31, 18, 40]
# even_counter = 0
# odd_counter = 0

# for num in numbers:
#     if num % 2 == 0:
#         even_counter += 1
#     else:
#         odd_counter += 1

# print(f'Even numbers: {even_counter}')
# print(f'Odd numbers: {odd_counter}')

numbers = [12, 45, 2, 67, 34, 89, 21]
max_number = 0

for i in range(len(numbers)):
    for j in range(len(numbers)):
        if numbers[i] > numbers[j]:
            if max_number < numbers[i]:
                max_number = numbers[i]
            
print(max_number)