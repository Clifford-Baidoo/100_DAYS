#Grade thingy
score = int(input("What is your score > "))

percentage = round(score/100 * 50,2)


if score > 100:
    print("Enter your correct score which should be below 100")
else:
    if percentage <= 10 :
        print("You got a grade of E ")
    elif percentage > 10 and percentage < 21 :
        print("You got a grade of D")
    elif percentage > 20 and percentage < 31 :
        print("You got a grade of c")
    elif percentage > 30 and percentage < 41 :
        print("You got a grade of B")
    elif percentage > 40 and percentage < 51 :
        print("You got a grade of A")