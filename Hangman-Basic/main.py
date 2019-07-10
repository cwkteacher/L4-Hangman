# import libraries
import random

# Constants
MAX_GUESSES = 6

# Global Variables 
secret_word = '' 
letters_guessed = []

def get_word():
    words = ["apple", "orange", "python", "happy", "birthday", "random", "life", "string", "list"]
    word = random.choice(words)
    return word

def word_guessed():
    # Set up variables
# Set up variables
    global secret_word
    global letters_guessed
    
    for letter in secret_word:
        if not (letter in letters_guessed):
            return False
    
    return True

def print_guessed():
    global secret_word
    global letters_guessed
    guessed_word = []

    for letter in secret_word:
        if letter in letters_guessed:
            guessed_word.append(letter)
        else:
            guessed_word.append("-")
    print("".join(guessed_word))

def play_hangman():
    '''
    Plays the hangman game.
    '''
    global secret_word
    global letters_guessed
    mistakes_made = 0
    play_game = True

    # Choose a random word
    secret_word  = get_word()
    
    while play_game:
        print("You have %d guesses left." % (MAX_GUESSES - mistakes_made))
        print_guessed()
        
        # Get user input
        guess = input("Enter a letter: ").lower()
        while guess in letters_guessed:
            print("You have already guessed letter %s." % guess)
            guess = input("Enter a different letter: ").lower()
        
        # Check if letter is in word
        letters_guessed.append(guess)
        if guess in secret_word:
            print("There is a %s" % guess)
            if word_guessed():
                print(secret_word)
                print("You won!")
                play_game = False
        else:
            mistakes_made += 1
            print("There is no %s" % guess)
            if mistakes_made == MAX_GUESSES:
                print("Game over")
                play_game = False

play_hangman()
