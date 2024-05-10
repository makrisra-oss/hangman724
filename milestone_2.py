import random

# List of words for the game
WORD_LIST = ['apple', 'banana', 'orange', 'mango', 'pineapple']

# Randomly select a word from the list
selected_word = random.choice(WORD_LIST)

# Get user input
user_guess = input("Enter a single letter: ")

# Validate user input
if len(user_guess) == 1 and user_guess.isalpha():
    print("Good guess!")
    # You can add additional logic to check if the guessed letter is in the selected word
else:
    print("Oops! That is not a valid input. Please enter a single letter.")

# Print the word list and the selected word (for debugging purposes)
print(f"Word List: {WORD_LIST}")
print(f"Selected Word: {selected_word}")

