numbers = [6, 8, 9, 13]
sqlist = []
for number, number2 in zip(numbers, numbers):
    sqlist.append(number*number2)

print(f"The list with each element squared: {sqlist}")