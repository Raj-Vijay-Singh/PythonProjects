num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

operation = input("Enter +, -, * or /: ")

if operation == "+":
    print(f"The sum is {num1 + num2}.")

if operation == "-":
    print(f"The difference is {num1 - num2}.")

if operation == "*":
    print(f"The product is {num1 * num2}.")

if operation == "/":
    print(f"The quotient is {num1 / num2}.")