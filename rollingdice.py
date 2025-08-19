import random


choice = input("Roll the dice? (y/n): ")
while choice.lower() == 'y':
    print(f"({random.randint(1,6)}, {random.randint(1,6)})")
    choice = input("Roll the dice? (y/n): ")
    
    if not choice.lower() == 'y':
        print("Thanks for playing")
        break