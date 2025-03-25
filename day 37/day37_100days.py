
print("STAR WARS NAME GENERATOR\n")

fname = input("What is your first name > ")
sname = input("What is your last name > ")

new_fname = fname[:3]
new_sname = sname[:3]

n_fname = new_fname + new_sname

mother = input("What is your mother's name > ")
city = input("What city were you born in > ")

new_mother = mother[:3]
new_city = city[:3]
s_name = new_mother + new_city

print(f"Your Star wars name is {n_fname.capitalize()} {s_name.capitalize()}")
