### DAY 23 - SUBROUTINES
A subroutine tells the computer that a piece of code exits and to go run it over and over again

We can do that with the def function which means define
By putting codes in them we can call on it everytime we need it

```Python
def rollDice():
  import random
  dice = random.randint(1, 6)
  print("You rolled", dice)
```

#### DAY 23 - CHALLENGE
The daily challenfe is to create a subroutine with both a username and password
where a loop will run till the user gets the correct login information
Check [day23_100days.py](/day%2023/day23_100days.py) for the answer