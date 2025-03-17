### DAY 24 - PARAMETERS
Today we will add parameters to our subroutine by putting some values in the parenthesis
These parameters are called arguments

```Python
def whichCake(ingredient):
  if ingredient == "chocolate":
    print("Mmm, chocolate cake is amazing")
  elif ingredient == "broccoli":
    print("You what mate?!")
  else: 
    print("Yeah, that's great I suppose...")
```

With the ingredient parameter we can just add the ingredient name in when calling the function

```Python
wichCake(Chocolate)
```

### DAY 24 CHALLENGE 
Today's challenge is to create a program that asks the user for a dice roll and randomly chooses a side of the dice and prints it
Check [day24_100days.py](/day%2024/day24_100days.py)