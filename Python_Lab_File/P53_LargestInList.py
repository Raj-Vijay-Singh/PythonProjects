list = [-23,-56,-21,-77]
largest = list[0]

for number in list:
    if number > largest:
        largest = number

print(f"The largest number in the list is {largest}.")