import random

user_wins = 0
computer_wins = 0

options  = ["rock", "paper", "scissors"]


while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()

    if user_input == "q":
        break
    
    # LIST of strings containing rock paper scissors
    if user_input not in options:
        # continue will re-ask the user the question at the top of the loop
        continue

    random_number = random.randint(0,2)
    # rock: 0, paper: 1, scissors: 2
    computer_pick = options[random_number]
    print("Computer picked", computer_pick + ".")

    # Check cases in which user wins
    if user_input == "rock" and computer_pick == "scissors":
        print("You won!")
        user_wins += 1
        continue

    elif user_input == "paper" and computer_pick == "rock":
        print("You won!")
        user_wins += 1
        continue

    elif user_input == "scissors" and computer_pick == "paper":
        print("You won!")
        user_wins += 1
        continue

    # Check case in which computer wins
    else:
        print("You lost!")
        computer_wins += 1
        

print("You won", user_wins, "times.")
print("The computer won")
print("Goodbye!")