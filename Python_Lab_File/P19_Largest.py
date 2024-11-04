num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

# Using conditional statements
if num1 > num2 and num1 > num3:
    print(f"{num1} is the largest out of the three.")

elif num2 > num1 and num2 > num3:
    print(f"{num2} is the largest out of the three.")

elif num3 > num1 and num3 > num2:
    print(f"{num3} is the largest out if the three.")

elif num1 == num2 == num3:
    print(f"All numbers are equal. {num1} is the largest.")

else:
    print("Two numbers are equal.", end=" ")
    if num1 == num2 or num1 == num3:
        print(f"{num1} is the largest out of the three.")
    else:
        print(f"{num2} is the largest out of the three.")

# Using max() function
print(f"Using max function, {max(num1, num2, num3)} is found to be the greatest out of three.")
