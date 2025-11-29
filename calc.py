num_1= float(input("Enter the first number: "))
num_2 = float(input("Enter the second number: "))
op = input("Enter the operator: ")

if(op == '+'):
    result = num_1 + num_2
elif(op == '-'):
    result = num_1 - num_2
elif(op == '*'):
    result = num_1 * num_2
elif(op == '/'):
    if(num_2 == 0):
        result = "Second number cannot be zero"
    else:
        result = num_1 / num_2
elif(op == '%'):
    if(num_2 == 0):
        result = "Second number cannot be zero"
    else:
        result = num_1 % num_2

print(f"{result}")

