num = int(input("Enter a number: "))
prime = True

for i in range(2, num,):
    if num%i == 0:
        prime = False
    i += 1

if prime:
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")