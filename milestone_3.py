import random

# List of words for the game
WORD_LIST = ['apple', 'banana', 'orange', 'mango', 'pineapple']

# Randomly select a word from the list
secret_word = random.choice(WORD_LIST)

def check_guess(guess):
    # Step 2: Convert the `guess` into lower case
    guess = guess.lower()

    # Step 3: Move the code that you wrote to check if the guess is in the word into this function block
    if guess in secret_word:
        print(f"Good guess! {guess} is in the word.")
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")

def ask_for_input():
    # Step 2: Move the code that you wrote in the `Iteratively check if the input is a valid guess` task into this function block
    while True:
        guess = input("Guess a letter: ")

        if len(guess) == 1 and guess.isalpha():
            # Step 3: Outside the while loop, but within this function, call the `check_guess` function to check if the guess is in the word
            check_guess(guess)
            break
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")

# Step 4: Outside the function, call the `ask_for_input` function to test your code
ask_for_input()

print("Thanks for playing!")

