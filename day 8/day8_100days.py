print("Wholesome Positivity Machine\n")

name = input("Who are you > ")
achieve = input("What do you want to achieve > ")
scale = int(input("On a scale of 1 - 10 how do you feel today > "))

if scale == 1:
    print(f"Hello {name} , no matter what is wrong keep your head up so that you can {achieve} today")
elif scale == 2:
    print(f"Hello {name}, do not give up keep fighting now")
elif scale == 3:
    print(f"Hello {name}, you are doing great keep pushing and try your best to achieve your goal of {achieve}")
elif scale == 4:
    print(f"Hello {name}, you are doing great , fight hard so that you can {achieve}")
elif scale == 5:
    print(f"You will be fine")
else:
    print("Input a correct value")