
import random


draw = {'S':'Scissors','P':'Paper','R':'Rock'}

def play():
    user = input("What's Your Choice ? 's' for Scissors, 'p' for Paper, and 'r' for Rock >>>  ").upper()
    computer = random.choice(list(draw))

    if user == computer :
        print("Computer choose " + draw[computer] + "And you choose " + draw[user]+".")
        return "It's a Tie"
    
    elif user_win(user,computer):
        print("Computer choose " + draw[computer] + "And you choose " + draw[user]+".")
        return "You Win !! "
    
    print("Computer choose " + draw[computer] + "And you choose " + draw[user]+".")
    return "You lose !! "

def user_win(user,computer):
    if(user=='S' and computer=='P') or (user=='P' and computer=='R') or (user=='R' and computer=='S'):
        return True
while True:

    print(play())

