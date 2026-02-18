import random

choices = ['rock','paper','scissors']
computerScore = 0
userScore = 0
toWin = 2
play = True

while play:
    while(computerScore < toWin and userScore < toWin):
        computer = random.choice(choices)
        user = input("Input rock, paper, or scissors: ").lower()
        print("The computer chose ")
        if(computer == user):
            print("Tie")
        elif(user == 'rock' and (computer == 'scissors' or computer == 'scissor')) or (user == 'paper' and computer == 'rock') or (user == 'scissors' and computer == 'paper'):
            print("You won that hand!")
            userScore += 1
        else:
            print("You lost that hand!")
            computerScore += 1
        print("Score is player:", userScore, "computer:", computerScore)

    if(userScore == toWin):
        print("You win!")
    else:
        print("The computer won :(")
    
    playAgain = input("Do you want to play again? [Y]es [N]o: ").lower()
    if playAgain == 'y':
        computerScore = 0
        userScore = 0
    else:
        play = False
        
