list1 = [10, 20, 30 ,40 , 50, 60]
print(f"The list is:\n{list1}.")
elem = int(input("Which element do you want to replace? Enter: "))

if elem in list1:
    list1[list1.index(elem)] = 2000
    print("The element was found and replaced.")
else:
    print("The element was not found, hence not replaced.")

print(f"The list is:\n{list1}")