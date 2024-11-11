while True:
    try:
        num = int(input("Enter a number: "))
        break

    except ValueError:
        print("You cannot enter anything except a number.\n")

print(f"Square of given number is: {num ** 2}")