import random
print("Infinity Dice 🎲\n")

roll = int(input("How many Sides > "))

def rolldice(roll):
    while True:
        rolls = random.randint(1,roll)
        print(f"You rolled {rolls}")

        choice = input("Roll again > ")
        if choice == "yes":
            continue
        else:
            break

rolldice(roll)