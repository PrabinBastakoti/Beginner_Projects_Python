
secret_word= input("Enter a Secret Word > ")
guess=""
guess_count=0
guess_limit=3
guess_left=3
out_of_guess= False

while guess != secret_word and not(out_of_guess):
    if guess_count < guess_limit:
        guess=input('Enter the word: ')
        guess_count += 1
        guess_left -=1
        if guess != secret_word and guess_left>0:
            print("Wrong Word, Try Again! \n You have " + str(guess_left) + ' tries left')
    else:
        out_of_guess=True
if out_of_guess:
    print('Wrong Word \nYou\'re Out Of Guesses, You Lose !!!')
else:
    print("Congrats, You Win !!!")    
        

         
    
