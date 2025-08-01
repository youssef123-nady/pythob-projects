# Simple Calculator

operator = input("Enter an operator (+ - * /): ")
try:
    num1 = float(input("Enter 1st number: "))
    num2 = float(input("Enter 2nd number: "))

    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            print("Error: Cannot divide by zero.")
    else:
        print("Error: Invalid operator! Please use +, -, *, or /.")

    print(f"Result: {num1} {operator} {num2} = {result}")

except ValueError:
    print("Error: Please enter valid numbers.")
