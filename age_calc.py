name = input("What is your name? ")
age = int(input("How old are you? "))

name = name.strip().title()
age_100 = 2125 - age

print(f"Hello {name}! \nYou are gonna turn 100 years old in year {age_100}.")