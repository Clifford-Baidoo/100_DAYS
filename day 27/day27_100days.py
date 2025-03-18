#LEGEND GENERATOR
import random , time , os

def health():
    six = random.randint(1,6)
    eight = random.randint(1,8)

    total_health = (six + eight)/2 + 10
    return round(total_health)

def stamina():
    six = random.randint(1,6)
    twelve = random.randint(1,12)

    total_stamina = (six + twelve)/2 + 10
    return round(total_stamina)

while True:
    os.system("cls")
    print("Character Builder\n")

    name = input("Name your legend > \n")
    char = input("Charcter Type (Human , Elf , Dwarf) > \n")

    os.system("cls")
    print(name)
    print(f"HEALTH : {health()}")
    print(f"STRENGTH : {stamina()}")

    print("May your name go down in Legend .....\n")
    time.sleep(5)

    question = input("Do you want to creater a new character (Y/N) > ")
    if question == "N":
        break
