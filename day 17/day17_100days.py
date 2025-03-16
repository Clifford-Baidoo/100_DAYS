from getpass import getpass as input


p1_Score = 0
p2_Score = 0

while True:
    print("ROCK PAPER SCISSORS")
    print("-------------------")

    p1 = input("Rock Paper Scissors? Choose one input R,P or S > ")
    p2 = input("Rock Paper Scissors? Choose one input R,P or S > ")

    if p1 == "S" and p2 == "P":
        print("P1 Wins")
        p1_Score += 1
    elif p1 == "R"and p2 == "S":
        print("P1 Wins")
        p1_Score += 1
    elif p1 == "P"and p2 == "R":
        print("P1 Wins")
        p1_Score += 1

    elif p2 == "S" and p1 == "P":
        print("P2 Wins")
        p2_Score += 1
    elif p2 == "R"and p1 == "S":
        print("P2 Wins")
        p2_Score += 1
    elif p2 == "P"and p1 == "R":
        print("P2 Wins")
        p2_Score += 1

    elif p1 == "R"and p2 == "R":
        print("It is a tie")
    elif p1 == "P"and p2 == "P":
        print("It is a tie")
    elif p1 == "S"and p2 == "S":
        print("It is a tie")
    else:
        print("Wrong input try again")

    print(f"Player 1 has {p1_Score} points")
    print(f"Player 2 has {p2_Score} points")

    if p1_Score == 3 or p2_Score == 3:
        if p1_Score == 3:
            print("Player 1 won with 3 points")
        else:
            print("Player 2 won with 3 points")
        print("Game Ended ")
        exit()