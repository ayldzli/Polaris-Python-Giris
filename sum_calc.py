def main():
    sumCalc(getInput())

def getInput():
    num = int(input("Enter the number:"))
    if num <= 1 :
        print("You must enter a number greater than 1")
        getInput()
    else:
        return num
    
def sumCalc(num):
    result = 0
    for i in range(num):
        result += num - i
    print(f"{result}")

main()