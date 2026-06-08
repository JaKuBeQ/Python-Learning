import random

options = ["rock", "paper", "scissors"]
computer_choice = random.choice(options)


print("choose rock, paper or scissors: ")
player_choice = input()

if player_choice == "rock":
    print("You chose rock")
    if computer_choice == "rock":
        print("Computer also chose rock\nIt's a tie!")
    elif computer_choice == "paper":
        print("Computer chose paper \nYou lose!")
    elif computer_choice == "scissors":
        print("Computer chose scissors \nYou win!")
elif player_choice == "paper":
    print("You chose paper")
    if computer_choice == "paper":
        print("Computer also chose paper\nIt's a tie!")
    elif computer_choice == "rock":
        print("Computer chose rock \nYou win!")
    elif computer_choice == "scissors":
        print("Computer chose scissors \nYou lose!")
elif player_choice == "scissors":
    print("You chose scissors")
    if computer_choice == "scissors":
        print("Computer also chose scissors \nIt's a tie!")
    elif computer_choice == "rock":
        print("Computer chose rock \nYou lose!")
    elif computer_choice == "paper":
        print("Computer chose paper \nYou win!")
else:
    print("Invalid input you need to choose rock, paper or scissors")


