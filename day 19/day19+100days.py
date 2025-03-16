#Loan Calculator

i = 0
amount = 1000
increase = 0.05

for i in range(0,11):
    percentage = amount * increase
    amount += percentage
    i+=1
    print(f"Year{i} is: {round(amount,2)} ")

