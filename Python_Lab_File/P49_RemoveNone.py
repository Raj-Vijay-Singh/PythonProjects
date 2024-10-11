list1 = ["Gloomy", 242, 87.42, None, "Eiffel Tower", None, None, 44, None]

def checknone(element):
    return element != None

new_elements = filter(checknone, list1)
list2 = list(new_elements)
print(f"New list without 'None' elements: {list2}")