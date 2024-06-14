# In Rock, Paper, Scissors, the winner is decided based on the rules of the game:

# Rock crushes Scissors (Rock wins)
# Scissors cuts Paper (Scissors win)
# Paper covers Rock (Paper wins)

# If both players choose the same item, it’s a tie. 

import random

choices = ['rock', 'paper', 'scissors']

def get_user_choice():
    user_choice = input("Enter your choice (rock, paper, or scissors): ")
    if user_choice.lower() not in choices:
        print("Invalid choice. Please enter rock, paper, or scissors.")
        return get_user_choice()
    return user_choice.lower()

def get_computer_choice():
    return random.choice(choices)

def display_choices(user_choice, computer_choice):
    print(f'User chose: {user_choice}')
    print(f'The computer chose: {computer_choice}')

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return 'tie'
    if user_choice == 'rock':
        return 'user' if computer_choice == 'scissors' else 'computer'
    if user_choice == 'scissors':
        return 'user' if computer_choice == 'paper' else 'computer'
    if user_choice == 'paper':
        return 'user' if computer_choice == 'rock' else 'computer'

def play_game():
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    display_choices(user_choice, computer_choice)
    winner = determine_winner(user_choice, computer_choice)
    if winner == 'tie':
        print('It\'s a tie!')
    else:
        print(f'{winner.capitalize()} wins!')

play_game()

