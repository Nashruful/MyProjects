board = ["-"] * 9

def print_board():
    print("|", board[0], "|", board[1], "|", board[2], "|")
    print("|", board[3], "|", board[4], "|", board[5], "|")
    print("|", board[6], "|", board[7], "|", board[8], "|")


def add(number, icon):
    number = int(number)
    if 9 >= number >= 1:
        if board[number - 1] == "-":
            board[number - 1] = icon
            return True
        else:
            print("this is already taken..")
            return False
    else:
        print("invalid input..")
        return False


def isDraw():
    if "-" not in board:
        return True
    else:
        return False


def isAwin(user_icon):
    if (board[0] == user_icon and board[1] == user_icon and board[2] == user_icon) or \
            (board[3] == user_icon and board[4] == user_icon and board[5] == user_icon) or \
            (board[6] == user_icon and board[7] == user_icon and board[8] == user_icon) or \
            (board[0] == user_icon and board[3] == user_icon and board[6] == user_icon) or \
            (board[1] == user_icon and board[4] == user_icon and board[7] == user_icon) or \
            (board[2] == user_icon and board[5] == user_icon and board[8] == user_icon) or \
            (board[0] == user_icon and board[4] == user_icon and board[8] == user_icon) or \
            (board[2] == user_icon and board[4] == user_icon and board[6] == user_icon):
        return True
    else:
        return False


print(print_board())
Player = "X"
while True:

    userr1 = input(f'{Player} Turn: ')

    if not userr1.isnumeric():
        print("invalid input..")
        continue
    if add(userr1, Player):
        print_board()
        if isAwin(Player):
            print(f'{Player} You win!')
            break
        elif isDraw():
            print("it's a Draw!")
            break
        Player = "O" if Player == "X" else "X"
    else:
        continue
