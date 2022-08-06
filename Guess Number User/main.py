

import random
number = random.randint(1,10)
while True:
    try:

        guess = int(input(" Guess a number between 1 and 10 > "))
        if guess == number :
            print(f"Yay, Congrats. You have guessed the number {number} correctly!!")
            break
        elif guess > number :
            print("Sorry, Guess again. Too high.")
        elif guess < number:
            print("Sorry, Guess again. Too low.")
    except ValueError:
        print(" Only Integers allowed.")