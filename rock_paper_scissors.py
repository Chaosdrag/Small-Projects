import random

if __name__ == '__main__':

    options = ('r', 'p', 's')
    emojis = {'r': '🪨', 'p': '📜', 's': '✂️'}
while True:
    user_choice = input('Rock, Paper, or Scissors? (r/p/s):').lower()
    if user_choice not in options:
        print('Invalid input')
        continue

    comp_choice = random.choice(options)

    print(f'You chose {emojis[user_choice]}')
    print(f'Computer chose {emojis[comp_choice]}')

    if user_choice == comp_choice:
        print('It\'s a tie!')
    elif (
        (user_choice == 'r' and comp_choice == 's')
        or (user_choice == 'p' and comp_choice == 'r')
            or (user_choice == 's' and comp_choice == 'p')):
        print('You win!')
    else:
        print('You lose!')

    cont = input('Do you want to play again? (y/n): ')
    if cont == 'n':
        break
