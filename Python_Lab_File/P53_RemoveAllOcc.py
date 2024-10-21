list1 = [10, 20, 1, 30, 10, 1, 1, 1, 89, 1, 89, 1]
print(f"The list is:\n{list1}")
dele = int(input("Enter the element you want to remove all occurrences of: "))

for i in range(list1.count(dele)):
    list1.remove(dele)

print(f"The list after all occurrences of {dele} removed is:\n{list1}")