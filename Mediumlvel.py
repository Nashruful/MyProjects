import fileinput
from cryptography.fernet import Fernet

Blue = '\033[94m'
Red = '\033[91m'
Reset = '\033[0m'
'''
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)'''


def load_key():
    file = open(r"C:\Users\azooz\PycharmProjects\HelloWorld\pythonProject2\key.key", "rb")
    keyy = file.read()
    file.close()
    return keyy


master_pwd = input("what is the Master PASSWORD!? : ")
key = load_key() + master_pwd.encode()
ferr = Fernet(key)


def view():
    with open('password.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("User: ", user, "| Password: ", ferr.decrypt(passw.encode()).decode())


def add():
    name = input("Account Name: ")
    pwd = input("Password: ")

    with open('password.txt', 'a') as f:
        f.write(name + "|" + ferr.encrypt(pwd.encode()).decode() + "\n")


while True:
    mode = input(
        f"Would you like to add a new password or view existing ones ({Blue}view{Reset},{Red}add{Reset}) press q to quit :  ").lower()
    if mode == "q" or mode == "quit":
        break

    elif mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode.")
        continue
