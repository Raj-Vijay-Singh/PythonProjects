a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))

if a > b and b > c:
    largest = a
elif b > a and b > c:
    largest = b
elif c > a and c > b:
    largest = c

print(f"The largest value out of {a}, {b} and {c} is: {largest}.")