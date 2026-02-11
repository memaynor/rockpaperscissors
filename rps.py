import random

choices = ["rock","paper","scissors"]
computerscore = 0
userscore = 0
winscore = 2

while(computerscore < winscore and userscore < winscore):
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
    print("Score is player:", userscore, "computer:", computerscore)

if(userscore == 2):
    print("You win!")
else:
    print("The computer won :(")
