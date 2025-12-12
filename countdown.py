from time import sleep

def main():
    num = getInput()
    while num != 0:
        print(num)
        sleep(1)
        num -= 1
    print("Boom!")

def getInput():
    try:
        input_num = int(input("Enter a number: "))
        if input_num <= 0:
            print("Enter a positive number.")
            getInput()
        else:
            return input_num
    except:
        print("Please enter a valid number.")
        getInput()

main()