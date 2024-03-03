from random import randint
play_option = ["rock" , "paper" , "scissors"]
CP = 0
UP = 0
i = 0

while i < 25000:
    i += 1
    if i == 25000:
        print(f'Your Wins = {UP}')
        print(f'Computer Wins = {CP}')
    computer_play = play_option[randint(0,2)]
    user_play ="rock"
    if computer_play == user_play:
        print("it's a tie!")
    elif user_play == "rock":
        if computer_play == "paper":
            print("Computer Wins! ")
            CP += 1
        else:
            print("You Win!")
            UP += 1
    elif user_play == "paper":
        if computer_play == "rock":
            print("You Win!")
            UP += 1
        else:
            print("Computer Wins!")
            CP += 1
    elif user_play == "scissors":
        if computer_play == "rock":
            print("Computer Wins!")
            CP += 1
        else:
            print("You Win!")
            UP += 1


    elif user_play == "quit":
        print(f'Your Wins = {UP}')
        print(f'Computer Wins = {CP}')
        break
    else:
        print("Invalid Input!")
