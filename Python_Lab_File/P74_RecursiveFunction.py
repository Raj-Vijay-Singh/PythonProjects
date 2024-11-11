def sum10(x = 0) :
    if x != 10:
        return x + sum10(x + 1)
    else:
        return x

print(f"Sum of numbers 1 to 10 is: {sum10()}")


