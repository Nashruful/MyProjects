import random
import time

top_of_range = input("Type a number: ")
guesses = 0
if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("enter a number that's higher than 0")
        quit()
else:
    print("please type a number only!")
    quit()

random_number = random.randint(0, top_of_range)
while True:
    guesses += 1
    user_guess = input("make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("enter a number!")
        continue

    if user_guess == random_number:
        print("Bingo!")
        break

    else:
        print("Wrong..", end=" ")
        differences = abs(user_guess - random_number)
        if differences > 25 and user_guess > random_number:
            print("you're too far! , go lower")
        elif differences > 25 and user_guess < random_number:
            print("you're too far! , go higher")
        elif user_guess > random_number:
            print("go lower")
        elif user_guess < random_number:
            print("go higher")
print("you got it in ", guesses, " guesses!")
s = f'the random generated number was {random_number}'
print(s.title())
