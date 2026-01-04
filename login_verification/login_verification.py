import re

weaknesses = []

def main():
    password = input("Please set your password: ")
    weakness = check_password(password)
    if (weakness):
        print("Your password is weak")
        print("Your password should include:")
        for i in weaknesses:
            print(i)
    else:
        print("Your password is strong")

def check_password(password):
    password = password.replace(" ", "")
    numbers = re.search(r"[0-9]", password)
    if (not numbers):
        weaknesses.append("numbers")
    lowercase_letters = re.search(r"[a-z]", password)
    if (not lowercase_letters):
        weaknesses.append("lowercase letters")
    uppercase_letters = re.search(r"[A-Z]", password)
    if (not uppercase_letters):
        weaknesses.append("uppercase letters")
    specials = re.search(r"[^a-zA-Z0-9]", password)
    if (not specials):
        weaknesses.append("special characters")
    if (numbers and lowercase_letters and uppercase_letters and specials):
        return False
    else:
        return True
    
if __name__ == "__main__":
    main()
