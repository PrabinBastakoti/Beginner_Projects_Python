import random
import time
import string
from words import words
from lives_visual_dict import lives_visual_dict
print("\n\t WELCOME TO HANGMAN !!")
time.sleep(2)

def get_valid_words(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()

def hangman():

    word = get_valid_words(words)
    word_letter = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    lives = 7 

    while len(word_letter) > 0 and lives > 0 :
        print("You have",lives,"lives left and you have used these words: ",' '.join(used_letters))
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print("Current word is: ",' '.join(word_list))
        print(lives_visual_dict[lives])
        user_letter = input("Guess a  letter : ").upper()

        if user_letter in alphabet - used_letters :
            used_letters.add(user_letter)
            if user_letter in word_letter:
                word_letter.remove(user_letter)
                print("You guess the correct letter",user_letter,'\n')
            else:
                lives -= 1
                print("Letter is not in the word",'\n')
        elif user_letter in used_letters:
            print("This letter is already Guessed. Try Guessing Another Letter.\n")
        else:
            print("Invalid Input. Try again.\n")
        time.sleep(2)

    if lives == 0 :
        print(lives_visual_dict[lives])
        print("You are dead, the word was",word,'\n')
    else:
        print("Yay! You guess the correct word",word,'\n')

hangman()

