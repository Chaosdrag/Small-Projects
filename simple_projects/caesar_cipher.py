# Encode a letter by shifting it by a number of places.
# Ask the user to enter the amount to be shifted.
# Ask the user to enter a word to encode.
# Print the encoded word.
# Add a check if the word goes past z or Z, if it does loop back to start.
# i.e. 'y' with a shift of 3 becomes 'b'.
# Allow for both uppercase and lowercase values.
# Check for incorrect inputs (e.g. entering a letter for shift).

# Get the shift amount and validate input
while True:
    try:
        shift = int(input("Enter the amount to shift by: "))
        break
    except ValueError:
        print("Please enter a valid integer for the shift amount.")

# Get the word to encode
encode = input("Enter a word to encode: ")

# Initialize the encoded word
encoded_word = ""

# Encode each letter
for letter in encode:
    if letter.isalpha():  # Check if the character is a letter
        if letter.islower():  # Handle lowercase letters
            encoded_word += chr((ord(letter) - 97 + shift) % 26 + 97)
        else:  # Handle uppercase letters
            encoded_word += chr((ord(letter) - 65 + shift) % 26 + 65)
    else:  # Keep non-alphabetic characters unchanged
        encoded_word += letter

# Print the encoded word
print(f"Encoded word: {encoded_word}")
