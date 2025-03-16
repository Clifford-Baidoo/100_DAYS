from getpass import getpass as input

print("ROCK PAPER SCISSORS")
print("-------------------")\

p1 = input("Rock Paper Scissors? Choose one input R,P or S > ")
p2 = input("Rock Paper Scissors? Choose one input R,P or S > ")

if p1 == "S" and p2 == "P":
    print("P1 Wins")
elif p1 == "R"and p2 == "S":
    print("P1 Wins")
elif p1 == "P"and p2 == "R":
    print("P1 Wins")

elif p2 == "s" and p1 == "P":
    print("P2 Wins")
elif p2 == "2"and p1 == "S":
    print("P2 Wins")
elif p2 == "P"and p1 == "R":
    print("P2 Wins")

elif p1 == "R"and p2 == "R":
    print("It is a tie")
elif p1 == "P"and p2 == "P":
    print("It is a tie")
elif p1 == "S"and p2 == "S":
    print("It is a tie")
else:
    print("Wrong input try again")