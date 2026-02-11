import random

choices = ["rock","paper","scissors"]
computerscore = 0
userscore = 0


while(computerscore < 2 and userscore < 2):
    computer = random.choice(choices)
    user = input("Input rock, paper, or scissors: ").lower()
    if(computer == user):
        print("Tie")
    elif(user == "rock" and computer == "scissors") or (user == "paper" and computer == "rock") or (user == "scissors" and computer == "paper"):
        print("You won that hand!")
        userscore += 1
    else:
        print("You lost that hand!")
        computerscore += 1

if(userscore == 2):
    print("You win!")
else:
    print("The computer won :(")
