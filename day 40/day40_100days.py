details = {"name":"","date":"","number":"","email":"","address":""}

name = input("Input your name > ")
date = input("Input your date of birth > ")
number = input("Input your telephone number > ")
email = input("Input your email > ")
address = input("Input your address > ")

print(f"""Hi {name}.Our dictionary says that you were born on {date}\n,we can call you on {number},email{email} , or write to {address}""")
