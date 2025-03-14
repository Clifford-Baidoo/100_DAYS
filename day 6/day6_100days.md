## ELIF

Today I learnt about elif statements which means else if or if else and it usually comes after the if statement

```Python
print("SECURE LOGIN")
username = input("Username > ")
if username == "mark"
    print("Welcome Mark")
else:
    print("Go away")
```

we are going to use the elif statement to expand this 
I will add an elif statement that will ask to see if the person is Suzanne
I will also add an and function which will add two parameters together 

```Python
print("SECURE LOGIN")
username = input("Username > ")
password = input("Password > ")
if username == "mark" and password == "password":
    print("Welcome Mark")
elif username == "suzanne" and password == "su7anne"
    print("Hey there Suzanne")
else:
    print("Go away")
```

So now the code will check to see if the username belongs to a suzanne before it ends

#### Daily Challenge
The daily challenge is to just use elif which I have done in the [day6_100days.py](/day%206/day6_100days.py) file