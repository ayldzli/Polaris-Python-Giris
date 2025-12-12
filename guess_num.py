from random import randint

def main():
    random_num = randint(1, 100)
    guess_num = getInput()
    while(guess_num != random_num):
        if guess_num > random_num: 
            print("Try smaller.")
            guess_num = getInput()
        elif guess_num < random_num:
            print("Try bigger.")
            guess_num = getInput()
    print("You guessed it right!")

def getInput():
    try:
        return int(input("Enter a number: "))
    except:
        print("Please enter a valid number.")
        getInput()

main()