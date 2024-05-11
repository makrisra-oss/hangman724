import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(self.word_list).upper()
        self.word_guessed = ['_'] * len(self.word)
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []

    def check_guess(self, guess):
        guess = guess.lower()
        if guess in self.word.lower():
            print(f"Good guess! {guess} is in the word.")
            for i, letter in enumerate(self.word.lower()):
                if letter == guess:
                    self.word_guessed[i] = letter.upper()
            self.num_letters -= 1
        else:
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word.")
            print(f"You have {self.num_lives} lives left.")

    def ask_for_input(self):
        while True:
            guess = input("Please guess a letter: ").lower()
            if len(guess) != 1 or not guess.isalpha():
                print("Invalid input. Please enter a single letter.")
            elif guess in self.list_of_guesses:
                print(f"You already guessed the letter {guess}. Please try again.")
            else:
                self.list_of_guesses.append(guess)
                self.check_guess(guess)
                break

def play_game(word_list):
    game = Hangman(word_list)
    max_lives = game.num_lives

    while True:
        if game.num_lives == 0:
            print(f"You ran out of lives. The word was: {game.word}")
            break
        elif game.num_letters > 0:
            game.ask_for_input()
        else:
            print(f"Congratulations! You guessed the word: {''.join(game.word_guessed)}")
            break

# Create a list of words
word_list = ['python', 'javascript', 'ruby', 'java', 'csharp']

# Call the play_game function and pass in the word_list
play_game(word_list)

    