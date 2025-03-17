import random
print("⚔️ Character Stats Generator ⚔️\n")

def roll1(side):
    result = random.randint(1 , side)
    return result

def roll2():
    six_side = roll1(6)
    eight_side = roll1(8)
    math = six_side * eight_side
    return math

while True:
    name = input("Name your warrior > ")
    print(f"The health is : {roll2()} \n")

    option = input("Do you want to make another character > ")
    if option == "yes":
        continue
    else:
        break


