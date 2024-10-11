def newton(num):
    temp = 0
    h = num / 2
    while abs(h - temp) > 0.00001:
        temp = h
        h = (h + (num/h)) / 2
    return round(h,10)

num = float(input("Enter the number: "))
print(f"Using Newton's method, the square is approximately {newton(num)}.")


