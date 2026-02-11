import random

choices = ['rock','paper','scissors']
computerScore = 0
userScore = 0
winningScore = 2

while(computerScore < winningScore and userScore < winningScore):
    computer = random.choice(choices)
    user = input("Input rock, paper, or scissors: ").lower()
    if(computer == user):
        print("Tie")
    elif(user == 'rock' and computer == 'scissors') or (user == 'paper' and computer == 'rock') or (user == 'scissors' and computer == 'paper'):
        print("You won that hand!")
        userScore += 1
    else:
        print("You lost that hand!")
        computerScore += 1
    print("Score is player:", userScore, "computer:", computerScore)

if(userScore == winningScore):
    print("You win!")
else:
    print("The computer won :(")
