### Nested IF Statements
Today I will be learning about nested if statements
That is just normal if statements but in another if statements

```Python
tvshow = input("What is your favorite tv show > ")

if tvshow == "peppa pig":
    print("Ugh why")
elif tvshow == "paw patrol":
    print("Aww, sad times")
else:
    print("Yeah,that's cool and all")
```
I will be adding some nested ifs to ask some questions in the original code above
```Python
tvshow = input("What is your favorite tv show > ")

if tvshow == "peppa pig":
    print("Ugh why")
    fav = input("Who is your favorite character > ")
    if fav == "daddy pig":
        print("Right Answer")
    else:
        print("Bozo")
elif tvshow == "paw patrol":
    print("Aww, sad times")
else:
    print("Yeah,that's cool and all")
```
I used nested ifs to ask another question about the users' favorite character in the tv show

#### Day 7 Challenge
I made a fake fan finder which I used nested if statement to do it
Check out [day7_100days.py](/day%207/day7_100days.py) to see it