import random

ROCK = 'r'
PAPER = 'p'
SCISSORS = 's'

emojis = {ROCK: '🪨', PAPER: '📜', SCISSORS: '✂️'}
options = tuple(emojis.keys())


def player_choice():
    while True:
        user_choice = input('Rock, Paper, or Scissors? (r/p/s):').lower()
        if user_choice in options:
            return user_choice
        else:
            print('Invalid input')


def display_choices(user_choice, comp_choice):
    print(f'You chose {emojis[user_choice]}')
    print(f'Computer chose {emojis[comp_choice]}')


def determine_winner(user_choice, comp_choice):
    if user_choice == comp_choice:
        print('It\'s a tie!')
    elif (
        (user_choice == ROCK and comp_choice == SCISSORS)
        or (user_choice == PAPER and comp_choice == ROCK)
            or (user_choice == SCISSORS and comp_choice == PAPER)):
        print('You win!')
    else:
        print('You lose!')


def play_game():
    while True:

        user_choice = player_choice()

        comp_choice = random.choice(options)

        display_choices(user_choice, comp_choice)

        determine_winner(user_choice, comp_choice)

        cont = input('Do you want to play again? (y/n): ')
        if cont == 'n':
            break


play_game()
