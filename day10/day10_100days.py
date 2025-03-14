print("Tip Calculator")
print("---------------")

bill = float(input("How much did you spend? "))
tip = int(input("What percentage do you want to tip? "))
split = int(input("How many people are in your group? "))

percentage = tip / 100
total_tip = bill * percentage
total_bill = round(bill + total_tip,2)

total_split = round(total_bill/split,2)

print(f"Your total bill is {total_bill}")
print(f"You each owe {total_split}")
