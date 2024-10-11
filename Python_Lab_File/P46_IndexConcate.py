list1 = ["Apples", "Mangoes", "Plums", "Cherries", "Pineapples"]
list2 = [20, 55, 89, 23, 1, 45, 88]
combined_list = []

for x, y in zip(list1, list2):
    combined_list.append(x)
    combined_list.append(y)

for x in list1:
    if x not in combined_list:
        combined_list.append(x)

for y in list2:
    if y not in combined_list:
        combined_list.append(y)

print(combined_list)