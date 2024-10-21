print("Printing using separate loops: ")
for i in range(6):
    print("*" * i)

for i in range(4,0,-1):
    print("*" * i)

# Using nested loop
max = 5
print("Printing using nested loop: ")
for i in range(1, max * 2):
    if i <= max:
        print("*" * i)
    else:
        print("*" * ((2*max) - i))