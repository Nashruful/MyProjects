import time
import random

sentence = ["the dog barks",
            "the cat meows",
            "the tiger roars",
            "the human talks"]
congratz = ["Good job!", "Well done", "You did it!"]
HS = 0
HSS = []

Blue = '\033[94m'
Red = '\033[91m'
Dark_Red = '\033[31m'
BOLD = '\033[1m'
Reset = '\033[0m'

timess = []

hot_streak_printed = False
fire_printed = False


def check_input(user_inputt, sentences):
    return user_inputt.lower() == sentences.lower()


def print_large(sentencess):
    large_text = {
        "the dog barks": r"""
         __        __  _                            _ 
         \ \      / /(_) ___    __ _  _ __    __ _ | |
          \ \ /\ / / | |/ __|  / _` || '_ \  / _` || |
           \ V  V /  | |\__ \ | (_| || | | || (_| ||_|
            \_/\_/   |_||___/  \__,_||_| |_| \__,_|(_)
        """,
        "the cat meows": r"""
          /\_/\    
         ( o.o )   
          > ^ <   
        """,
        "the tiger roars": r"""
        / \    / \   
       {   }  {   }  
        \ /    \ /     
        """,
        "the human talks": r"""
          \     /    
        ---*-*---   
          /     \   
        """
    }
    large_text_art = large_text.get(sentencess.lower(), "Not Found")

    print(large_text_art)


while True:
    current_sentence = sentence[random.randint(0, 3)]
    print(Blue + BOLD + current_sentence + Reset)
    # print_large(current_sentence)
    start_time = time.time()
    user_input = input(": ")
    end_time = time.time()

    time_taken = end_time - start_time
    # print(time_taken)
    if check_input(user_input, current_sentence):
        if time_taken <= 3:
            print(congratz[random.randint(0, 2)])
            HS += 1
            HSS.append(HS)
            timess.append(time_taken)

            if HS == 4:
                print(Red + "HOT STREAK!" + Reset)

            elif HS == 7:
                print(Dark_Red + " FIREEEEE!!" + Reset)
        else:
            print("you're too slow..")
            HS = 0
            continue

    elif user_input == "quit":
        break

    else:
        HS = 0
        print("wrong input")

print(f"you're lowest time taken was {min(timess)}")
print(f'your best streak was: {max(HSS)}')
