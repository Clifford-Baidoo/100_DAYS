print("One-Million-To-One")
print("------------------")

Number = 10000

while True:
    Guess = int(input("What is your guess > "))
    if Guess == 10000:
        print("You have Guessed the right number")
        break
    elif Guess > Number:
        print("Too High")
    elif Guess < Number:
        print("Too Low")
    else:
        print("Enter a number between one and one million")

print("Well done for Guessing the right number")