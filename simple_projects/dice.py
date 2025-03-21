import random


def dice(diceNum):
    rolls = [random.choice([1, 2, 3, 4, 5, 6]) for _ in range(diceNum)]
    total = sum(rolls)
    return rolls, total


count = 0

while True:

    play = input('Roll the dice? (y/n) :')
    if play == 'y':
        count += 1
        try:
            diceNum = int(input('How many dice? :'))
            if diceNum < 1:
                print('Invalid input! Please enter a number greater than 0')
                continue
            rolls, total = dice(diceNum)
            print(rolls, total)
            print(count)
        except ValueError:
            print('Invalid input! Please enter a number')
    elif play == 'n':
        print('Goodbye!')
        break
    else:
        print('Invalid input!')


# allow user to specify how many dice
# track no of times rolled during a session
