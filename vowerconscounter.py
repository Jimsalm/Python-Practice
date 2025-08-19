

vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
vowel_count = 0
consonant_count = 0

user_input = input("\nEnter a word or sentence: ")

for letter in user_input:
    if letter in vowels:
        vowel_count += 1
    elif letter.isalpha():
        consonant_count += 1

print(f'Vowels: {vowel_count}')
print(f'Consonant: {consonant_count}\n')
