# Choose a random letter between a and z
# Use math.random or random class to get a random value
# Ask the user to guess the letter
# If the user guesses correctly, print "Congratulations!"
# If the letter is close print "warm"
# If the letter is far print "cold"
# if the letter is very close print "hot"
# Keep playing until the user guesses the letter
# Keep track of the number of guesses

import random
import string

# guess counter
count = 0

# gen random lower case letter
answer = random.choice(string.ascii_lowercase)

while True:
    guess = input("Guess the letter :").lower()
    count += 1

    if not guess.isalpha() or len(guess) != 1:
        print("Please enter a single valid letter:")
        continue

    if guess == answer:
        print("Congratulations!")
        break
    else:
        distance = abs(ord(guess) - ord(answer))
        if distance == 1:
            print("Hot")
        elif distance <= 3:
            print("Warm")
        else:
            print("Cold")
