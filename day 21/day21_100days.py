print("MATH GAME !")
print("-----------\n")

multiplier = int(input("Name your multiples: "))
score = 0
for i in range (1,13):

    answer = int(input(f"{i} x {multiplier} > "))
    if answer == i * multiplier:
        score += 1
        print("Great Work\n")

    else:
        print("Nope the Correct anser is ", i*multiplier)
        print("")

print("---\n")
print(f"You scored {score}/12")