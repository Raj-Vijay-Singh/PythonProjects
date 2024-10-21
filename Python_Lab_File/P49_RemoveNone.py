list1 = ["Gloomy", 242, 87.42, None, "Eiffel Tower", "", None, 44, ""]

new_elements = filter(None, list1)
list2 = list(new_elements)
print(f"New list without 'None' elements: {list2}")