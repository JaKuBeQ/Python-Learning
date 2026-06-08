import random

options = ["rock", "paper", "scissors"]
computer_choice = random.choice(options)


print("choose rock, paper or scissors: ")
player_choice = input().lower()

if player_choice not in options:
    print("Invalid input. You need to choose rock, paper or scissors.")
else:
    print("You chose:", player_choice)
    print("Computer chose:", computer_choice)

    if player_choice == computer_choice:
        print("It's a tie!")
    elif player_choice == "rock" and computer_choice == "scissors":
        print("You win!")
    elif player_choice == "paper" and computer_choice == "rock":
        print("You win!")
    elif player_choice == "scissors" and computer_choice == "paper":
        print("You win!")
    else:
        print("You lose!")




