board = ["-"] * 9


def print_board():
    print(f"| {board[0]} | {board[1]} | {board[2]} | ")
    print(f"| {board[3]} | {board[4]} | {board[5]} | ")
    print(f"| {board[6]} | {board[7]} | {board[8]} | ")


def user_play(user_icon):
    print("Your chance to play:", user_icon)
    user_choice = int(input("Enter A Number from 1-9: "))

    if board[user_choice -1] == "-":
        board[user_choice -1] = user_icon
    else:
        print("this space is already taken!")



def is_victory(user_icon):
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

def is_draw():
    if "-" not in board:
        return True
    else:
        return False

while True:
    print_board()
    user_play('X')
    print_board()

    if is_victory('X'):
        print("X Wins!")
        break
    elif is_draw():
        print("It's a draw!")
        break

    user_play('O')
    print_board()

    if is_victory('O'):
        print("O Wins!")
        break
    elif is_draw():
        print("It's a draw!")
        break

