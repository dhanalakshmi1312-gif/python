a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
operation = input("Enter operator (+, -, *, /): ")

if operation == '+':
    print("Result:", a + b)
elif operation == '-':
    print("Result:", a - b)
elif operation == '*':
    print("Result:", a * b)
elif operation == '/':
    if a or b != 0:
        print("Result:", a / b)
    else:
        print("Division by zero not allowed")
else:
    print("Invalid operator")
