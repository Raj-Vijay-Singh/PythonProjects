num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second numer: "))

upper = min(num1, num2)

for i in range(1, upper+1):
    if num1%i == 0 and num2%i == 0:
        GCD = i

print(f"Greatest Common Divisor of {num1} and {num2} is {GCD}.")