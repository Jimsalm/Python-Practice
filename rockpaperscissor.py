import random

rock_paper_scissors = {
    "r" : "🪨",
    "p" : "🧻",
    "s" : "✂️"
}

isPlaying = True

while isPlaying:
    computer_choice = random.choice(["r", "p", "s"])
    player_choice = input("Rock, paper, or scissors? (r/p/s): ").lower()
    result = ""
    
    if player_choice == computer_choice:
        result = "Tie"
    elif (player_choice == 'r' and computer_choice == 's') or (player_choice == 'p' and computer_choice == 'r') or (player_choice == 's' and computer_choice == 'p'):
        result = "You Win"
    elif (player_choice == 'r' and computer_choice == 'p') or (player_choice == 'p' and computer_choice == 's') or (player_choice == 's' and computer_choice == 'r'):
        result = "You Lose"
    else:
        print("Invalid Choice")
        continue
    
    print(f"Computer chose {rock_paper_scissors[computer_choice]}")
    print(f"You chose {rock_paper_scissors[player_choice]}")
    print(result)
    
    continue_play = input("Continue? (y/n)").lower()
    if continue_play == 'y':
        isPlaying = True
    elif continue_play == 'n':
        isPlaying = False
    else:
        print("Invalid Choice")
        isPlaying = False
