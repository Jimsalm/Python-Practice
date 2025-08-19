import random

lowercase_character = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
uppercase_character = ['H', 'I', 'J', 'K', 'L', 'M', 'N']
number_character = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
symbol_character = ['!', '@', '#', '%', '$']
generated_password = []
all_character = [lowercase_character, uppercase_character, number_character, symbol_character]


password_lenght = int(input("How long would you like your password to be? "))

for i in range(password_lenght):
    generated_password.append(random.choice(random.choice(all_character)))
    print(generated_password)

NEW_PASSWORD = "".join(generated_password)
    
print(f'Your new password is : {NEW_PASSWORD}')