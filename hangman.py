import random


words = ['python', 'computer', 'program', 'keyboard', 'science', 'variable', 'function', 
         'developer','terminal', 'algorithm', 'internet', 'database', 'framework', 'website', 'security']

random_word = random.choice(words)
print(random_word)
guesses_left = 6
guessed_answer = []

for char in random_word:
    guessed_answer.append("_")

while True:    
    for char in guessed_answer:
        print(char, end=" ")
    
    user_input = input("\nGuess a letter to complete the word: ")
      
    if user_input in random_word:
        print("\nYou guessed a correct letter, guess again")
        for i in range(len(random_word)):
            if user_input == random_word[i]:
                guessed_answer.pop(i)
                guessed_answer.insert(i, user_input)
    elif user_input not in random_word:
        guesses_left -= 1
        print(f'\n Incorrect. You have {guesses_left} more guess remaining.')   
        
    if ''.join(guessed_answer) == random_word:
        print("\nCongrats you guessed the correct word 😍")
        break
    elif guesses_left == 0:
        print("Game Over, no remaining guesses. 😒")
        break