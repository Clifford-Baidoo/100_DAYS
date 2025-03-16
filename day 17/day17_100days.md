### DAY 17 - ANOTHER CHEAT CONTINUE
I learnt that you can use the break function to break out of a while loop but you can also use a continue function to continue
Which is good when you are creating games
So depending on the users choice the game will either stop or continue like the piece of code below

```Python
while True:
  print("You are in a corridor, do you go left or right?")
  direction = input("> ")
  if direction == "left":
    print("You have fallen to your death")
    break
  elif direction == "right":
    continue
  else:
    print("Ahh! You're a genius, you've won")
```

Adding the exit command completely stops the code from running when you are done with what you want to do
```Python
while True:
  print("You are in a corridor, do you go left or right?")
  direction = input("> ")
  if direction == "left":
    print("You have fallen to your death")
    break
  elif direction == "right":
    continue
  else:
    print("Ahh! You're a genius, you've won")
    exit()
print("The game is over, you've failed!")
```

#### DAY 17 CHALLENGE
Fixing the errors in a code