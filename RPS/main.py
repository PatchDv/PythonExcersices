import random

options = ("rock", "paper", "scissors")
isRunning = True


playerScore = 0
computerScore = 0

while isRunning:

    player = None
    computer = random.choice(options)

    while player not in options:

        
        print("------SCORE------")
        print(f"Player: {playerScore} | Computer: {computerScore}")
        
        player = input("Enter your choice (rock, paper, scissors): ").lower()

    print(f"Player: {player}")
    print(f"Computer: {computer}")

    if player == computer:
        print("It's a tie!")
    elif (player == "rock" and computer == "scissors"):
        print("You win!")
        playerScore += 1
    elif (player == "scissors" and computer == "paper"):
        print("You win!")
        playerScore += 1
    elif (player == "paper" and computer == "rock"):
        print("You win!")
        playerScore += 1
    else:
        print("You lose!")
        computerScore += 1

    play_again = input("Do you want to play again? (y/n): ").lower()
    if play_again != "y":
        isRunning = False
        print("------ FINAL SCORE ------")
        print(f"Player: {playerScore} | Computer: {computerScore}")
        print("Thanks for playing!")