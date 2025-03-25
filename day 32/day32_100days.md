### DAY 32 - LISTS
Lists are just list of items
Any piece of data can be put in a list which can be extracted removed or changed

lists are zero indexed which means the program starts counting from 0

Lists can be accessed by using the index

Lists can be defined using square brackets and seperating them with commas
```Python
timetable = ["Computer Science","Math","English","Art","Sport"]
print(timetable)
```
To avoid printing everything indexes are used
If I wanted to print just math I would do it like this:
```Python
print(timetable[2])
```
#### Changing Lists
Lists can be changed anytime you want
```Python
timetable[4] = "Watch TV"
```
Just define the index of the timetable and change it by inputing the new parameter

#### Loops and Lists
Loops can be used for lists which is a better way of printing stuff in a list
```Python
for lession in timetable:
    print(lesson)
```

#### DAY 32 - CHALLENGE
The challenge is to store a list of greetings and at random print out one of the greetings
Check[day32_100days.py](/day%2032/day32_100days.py) for the solution
