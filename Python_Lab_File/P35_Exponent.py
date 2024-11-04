num = int(input("Enter the number: "))
exp = int(input(f"Enter the power {num} should be raised to: "))

# Using pow() function
print(f"Using pow() function: {num} raised to the power of {exp} is {pow(num, exp)}.")

# Using ** operator
print(f"Using ** operator: {num} raised to the power of {exp} is {num ** exp}.")