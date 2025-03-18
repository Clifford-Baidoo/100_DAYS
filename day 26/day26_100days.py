import os , time

while True:
    print("🎵 MyPOD Music Player🎵\n")

    print("Press 1 to Play")
    print("Press 2 to Exit \n ")

    choice = input("Press anything else to see the menu > ")

    if choice == "1" :
        print("Playing some proper tunes")
        time.sleep(5)
        os.system("cls")

    elif choice == "2":
        print("Bye Bye")
        break
    else:
        os.system("cls")
        continue

