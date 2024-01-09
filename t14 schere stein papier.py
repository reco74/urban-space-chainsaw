import random

user_action = input("Enter a choice (rock, paper, scissors): ")
possible_actions = ["rock", "paper", "scissors"]
computer_action = random.choice(possible_actions)
if user_action in possible_actions:

    print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")

    if user_action == computer_action:
        print("Its a tie")
    elif user_action == "rock" and computer_action == "paper":
        print("You Lost")
    elif user_action == "rock" and computer_action == "scissors":
        print("You Won")
    elif user_action == "paper" and computer_action == "scissors":
        print("You Lost")
    elif user_action == "paper" and computer_action == "rock":
        print("You Won")
    elif user_action == "scissors" and computer_action == "rock":
        print("You Lost")
    elif user_action == "scissors" and computer_action == "paper":
        print("You Won")
else:
    print("Ungültige Eingabe")

