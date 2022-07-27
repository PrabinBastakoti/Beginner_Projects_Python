
import random

def computer_guess(x):
    low = 1
    high = x 
    feedback = ''
    while feedback != 'c' and 'C':
        if low != high :
            guess = random.randint(low, high)
        else :
            guess = low # could be high as well since low = high
        feedback= input(f"Is {guess} too High ( H ), too Low ( L ), or correct ( C ) ?? ")
        if feedback == 'h' and 'H':
            high = guess - 1

        if feedback == 'l' and 'L':
            low = guess + 1
        
    print(f"Yay! The computer guessed your number, {guess}, correctly!")

computer_guess(1000)