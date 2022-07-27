
import random
draw = {"r":"Rock","p":"Paper","s":"Scissors"}

def play():

    user = input("What's your choice? 'r' for Rock, 'p' for Paper, 's' for Scissors >>> ").lower()


    computer = random.choice(list(draw))

    if user == computer:
        print("Computer choose " + draw[computer] + " and You choose " + draw[user] + ".")
        return 'It\'s a Tie.'
    
    elif user_win(user,computer):
        print("Computer choose " + draw[computer] + " and You choose " + draw[user] + ".")
        return 'You Won !'
    
    print("Computer choose " + draw[computer] + " and You choose " + draw[user] + ".")
    return 'You Lose !'

def user_win(player,opponent):
    if (player == 'p'and opponent == 'r') or (player == 'r'and opponent=='s') or (player == 's'and opponent == 'p'):
        return True
    
while True:

    print(play())

        

   

    