print("REPLIT LOGIN SYSTEM")
print("-------------------\n")

def login():
    while True:
        username = input("What is your username > ")
        passwd = input("What is your password > ")

        if username == "admin" and passwd == "pfsense":
            print("Welcome to Replit!\n")
            break
        else:
            print("Whoops! I don't recognize that username or password. Try again!")

login()
