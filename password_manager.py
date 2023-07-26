# IMPORT 
from cryptography.fernet import Fernet

# MASTER PASS INPUT
master_pwd = input("What is the master password? ")

# FUNCTIONS
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)


def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("User: ", user, ", Password: ", passw)

def add():
    name = input('Account Name: ')
    pwd = input("Password: ")

    with open('passwords.txt', 'a') as f:
        # WITH open - opens and automatically closes files
        # MODES w (write/overwrite), r (read), a (append)
        f.write(name + "|" + pwd + "\n")

# LOOP
while True:
    mode = input("Whould you like to add a new password or view existing ones (view, add)? Press q to quit. ")

    if mode == "q":
        break

    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode.")
        continue

