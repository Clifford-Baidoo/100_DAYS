import os, time, random

todo = []

#Inputing choice
print("Welcome to your TODO List\n")


#View function
def view():
    counter = 1
    for i in todo:
        print(f"{counter}.{i}")
        counter += 1
#Code for adding and allat
while True:
    os.system("cls")
    choice = input("Do you want to \n1.View\n2.Add\n3.Remove\n4.Edit\n > ")
    if choice == "1":
        os.system("cls")
        view()
        time.sleep(2)
    elif choice == "2":
        adding = input("What task do you want to add > ")
        if adding in todo:
            print("Item already exits")
        else:
            todo.append(adding)
    elif choice == "3":
        removing = input("What do you want to remove > ")
        if removing in todo:
            todo.remove(removing)
        else:
            print("Item not found")
    elif choice == "4":
        print("What do you want to edit")
        view()
        time.sleep(2)
        num = int(input("Select the number > "))
        message = input("Enter new item > ")
        todo[num] = message
    else:
        print("Invalid Input")
