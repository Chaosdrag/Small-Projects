import random


def dice(x, y):
    dice1 = random.choice(x)
    dice2 = random.choice(y)
    return dice1, dice2, dice1+dice2


x = [1, 2, 3, 4, 5, 6]
y = [1, 2, 3, 4, 5, 6]


while True:

    play = input('Roll the dice? (y/n) :')

    if play == 'y':
        dice1, dice2, total = dice(x, y)
        print((dice1, dice2), total)

    elif play == 'n':
        print('Goodbye!')
        break
    else:
        print('Invalid input!')


# allow user to specify how many dice
# track no of times rolled during a session
