dict = {"Daksh": 78,
        "Siksha": 65,
        "Parveen": 32,
        "Lalit": 98,
        "Varsha": 86}

key = "Daksh"

for (x, y) in zip(dict.keys(), dict.values()):
    if y < dict[key]:
        key = x

print(f"The key with the minimum value: {key}")