import os

items = []
choice = input("Do you want view , add or remove from the list > ")


while True:
    choice = input("Do you want view , add or remove from the list > ")
    if choice == "view":
        for i in items:
            print(i)
    elif choice == "add":
        addition = input("Type what you want to add > ")
        items.append(addition)
    elif choice == "remove":
        sub = input("What item do you want to remove > ")
        if sub in items:
            items.remove(sub)
        else:
            print("There is no item like that in the list")
    else:
        print("Bye Bye")
        exit()