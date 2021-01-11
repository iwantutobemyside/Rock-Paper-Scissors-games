from random import randint
bot = ["Rock", "Paper", "Scissors"]
computer = bot[randint(0,2)]
player = False
while player == False:
    player = input("Rock, Paper, Scissors? : ")
    if player == computer:
        print("It's Tie!!","becoz", "computer = ",computer)
    elif player == "Rock":
        if computer == "Paper":
            print("You lose!", "becoz", "computer = ",computer)
        else:
            print("You win!", "becoz", "computer = ",computer)
    elif player == "Paper":
        if computer == "Rock":
            print("You win!", "becoz", "computer = ",computer)
        else:
            print("You lose!", "becoz", "computer = ",computer)
    elif player == "Scissors":
        if computer == "Rock":
            print("You lose!", "becoz", "computer = ",computer)
        else:
            print("You win!", "becoz", "computer = ",computer)
    else:
        print("Not a Valid play bro, Pls check ur spelling")
player = False
computer = bot[randint(0,2)]