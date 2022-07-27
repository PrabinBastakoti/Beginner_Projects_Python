from random import randint 

t=["Rock","Paper","Scissors"]

computer = t[randint(0,2)]
player = True

while player == True:
    player=input("Rock, Paper, Scissors? ")
    if player == computer:
        print("Tie!")
    elif player == "Rock":
        if computer=="Paper":
            print("You lose!", computer, "covers", player)
        else:
            print("You win!", player, "smashes", computer)
    elif player=="Paper":
        if computer=="Rock":
            print("You win!", player, "covers", computer)
        else:
            print("You lose!", computer, "cuts", player)
    elif player=="Scissors":
        if computer=="Rock":
            print("You lose!", computer, "smashes", player)
        else:
            print("You win!", player, "cuts", computer)
    else:
        print("That's not a valid play. Check your spelling!")
        
    player = True

   
