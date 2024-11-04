max = 5
print("Printing using nested loop: ")
for i in range(1, max * 2):
    if i <= max:
        print("*" * i)
    else:
        print("*" * ((2*max) - i))