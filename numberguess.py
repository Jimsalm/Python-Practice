import random


random_num = random.randint(1,100)
isGuessed = False

while isGuessed == False:
    guess_num = int(input("Guess the number between 1 - 100: "))   
    if guess_num > random_num:
        print("Too high!")       
    elif guess_num < random_num:
        print("Too low!")   
    elif guess_num == random_num:
        print("Congrats! You guessed the number.")
        isGuessed = True
    else:
        print("Please enter a valid number")
        