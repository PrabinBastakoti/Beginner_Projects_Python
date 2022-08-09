import random 
print("What is your name? ")
name = input()
print(f"Well,{name}, I am thinking of a number try to guess it.")

computer = random.randint(1,20)
guess = None
for guess_taken in range(1,7):
    try:
        # checks for input type
        guess = int(input("Take a Guess : "))
    except ValueError:
        print("You did not typed a number moron.")
        continue # go to the begining of the loop

    if guess > computer:
        print("Your Guess is too high.")
    elif guess < computer:
        print("Your guess is too low.")
    else:
        break
if guess == computer:
    print(f"You guessed the correct number {computer} in {guess_taken} chances.")
else:
    print(f"You are out of chances. The number is {computer}.")
