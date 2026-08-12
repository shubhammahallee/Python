from random import randint

play_options = ["scissors","paper","rock"]

while True:
    computer_play = play_options[randint(0,2)]
 
    user_input = input("Enter your choice (rock,paper,scissors):").lower()
    if user_input not in play_options:
        continue
    
    if user_input == computer_play:
        print("Tie")
    elif user_input == "rock":
        if computer_play == "scissors":
            print("you Win")
        else:
            print("Computer Win")
    elif user_input == "paper":
        if computer_play == "rock":
            print("you Win")
        else:
            print("Computer Win")
    elif user_input == "scissors":
        if computer_play == "paper":
            print("you Win")
        else:
            print("Computer Win")

    play_again = input("Play Again? (y/n): ").lower()
    if play_again != "y":
        break
