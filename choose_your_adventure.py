name = input("Type your name: ")
print("Welcome", name , "to this adventure!")

Blue = '\033[94m'
Red = '\033[91m'
Reset = '\033[0m'

answer = input("you're on a dirt road , go "+ Blue + "left" + Reset + " or " + Red + " right " + Reset + ": " ).lower()

if answer == "left":
    answer = input(
        "you come to a river , you can walk around it or swim across? Type{0} walk {1}to walk around and {2} swim {3} "
        "to swim across : ".format(
            Blue, Reset, Red, Reset)).lower()

    if answer == "swim":
        print("you swam acrross and were eaten by an alligator.")
    elif answer == "walk":
        print("you walked by many miles , ran out of water , you lost the game!")
    else:
        print("not a valid option... you lose!")

elif answer == "right":
    answer = input(f'You came to a bridge, it looks wobbly, do you want to {Blue}cross{Reset} it or head {Red}back{Reset} ? : ')
    print()
    if answer == "back":
        print(f'You go back and lose')
    elif answer == "cross":
        answer = input(f'You cross the bridge and meet a stranger. Do you want to talk to them {Blue}Yes{Reset}/{Red}No{Reset} : ').lower()
        if answer == "yes":
            print("you talk to the stranger and they give you gold. You WIN!")
        elif answer == "no":
            print("you ignored the Stranger and they are offended. You lose..")
        else:
            print("not a valid option... you lose!")
    else:
        print("not a valid option... you lose!")
else:
    print("not a valid option.. you lose :D")

print("Thank you for trying!", name)
