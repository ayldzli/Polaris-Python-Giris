def main():
    print(f"Number is {get_num()}.")
    
def get_num():
    try:
        return int(input("Enter a number: "))
    except:
        print("Please enter a valid number.")
        get_num()

main()