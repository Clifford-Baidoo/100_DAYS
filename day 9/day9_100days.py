print("Generation Identifier")
print("--------------------")

year = int(input("What year were you born in? "))

if year > 1882 and year < 1900:
    print("You are a part of the Lost Generation")
elif year > 1900 and year < 1925:
    print("You are a part of the Greatest Generation")
elif year > 1924 and year < 1945:
    print("You are a part of the Silent Generation")
elif year > 1944 and year < 1965:
    print("You are a part of the Baby Boomer Generation")
elif year > 1964 and year < 1980:
    print("You are a part of Generation X")
elif year > 1979 and year < 1995:
    print("You are a part of the Millennial Generation")
elif year > 1994 and year < 2010:
    print("You are a part of Generation Z")
else:
    print("You are a part of Generation Alpha")


