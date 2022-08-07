
import random

def computer_guess(x):
    low = 1
    high = x 
    feedback = ''
    while feedback != 'c' or feedback ==  'C':
        if low != high :
            guess = random.randint(low, high)
        else :
            guess = low # could be high as well since low = high
        feedback= input(f"Is {guess} too High ( H ), too Low ( L ), or correct ( C ) ?? ")
        if feedback == 'h' or feedback == 'H':
            high = guess - 1

        elif feedback == 'l' or feedback== 'L':
            low = guess + 1
        
    print(f"Yay! The computer guessed your number, {guess}, correctly!")

computer_guess(1000)