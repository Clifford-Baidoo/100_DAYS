## Name App
import os,time
name = []

def view():
    counter = 1
    for i in name:
        print(f"{counter}.{i}")
    counter += 1

while True:
    os.system("cls")
    first = input("What is your first name > ").title().strip()
    last = input("What is your last name > ").title().strip()

    
    full_name = f"{first} {last}"
    if full_name in name:
        print("Error Duplicate Detected")
        break
    else:
        name.append(full_name)
        view()
        time.sleep(2)
        choice = input("Do you want to add another name > ").lower()
        if choice == "yes":
            continue
        else:
            break

