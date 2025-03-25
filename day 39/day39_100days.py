import os , random , time
listOfWords = ["british", "suave", "integrity", "accent", "evil", "genius", "Downton"]
chosen = []
lives = 6
choice = random.choice(listOfWords)


while True:
    time.sleep(2)
    os.system("cls")
    guess = input("Choose a letter > ")
    if guess in chosen:
        print("You've used the letter")
        continue
    chosen.append(guess)

    if guess in choice:
        print("Correct")
    else:
        print("Nope, not correct")
        lives -= 1

    letters = True
    print()
    for i in choice:
        if i in chosen:
            print(i,end="")
        else:
            print("_",end="")
            letters = False
    print()

    if letters:
        print(f"You have won with {lives} lives left")
        break

    if lives <= 0:
        print(f"You have run out of lives! The anser was {choice}")
        break
    else:
        print(f"Only {lives} left")
    