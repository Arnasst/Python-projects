import random
import string
from words import words # these are random words that can be chosen to play with

def get_valid_word(words):
    word = random.choice(words) # chooses a random word from the given list
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set() # what already has been quessed

    lives = 6 #how many mistakes are allowed

    while len(word_letters) > 0 and lives > 0:
        print('You have', lives, 'lives left and you have already quessed: ', ' '.join(used_letters))
        # ' '.join(['a', 'b', 'cd']) --> 'a b cd'
        #what current word is
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word is ', ' '.join(word_list))

        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives -= 1
                print('Letter is not in the word')

        elif user_letter in used_letters:
            print("You already tried it")
        else:
            print('Invalid input')
            
    if lives == 0:
        print('You lost, the word was', word)
    else:   
        print('You won, the word was', word,)

    
hangman()
