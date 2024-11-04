albums = {"Fearless": 2008, "1989": 2014, "Reputation": 2017, "folklore": 2020, "evermore": 2021, "Midnights": 2022}

# Adding element
albums["Red"] = 2012
print(albums)

# Remove element
albums.pop("Fearless")
print(albums)

# Edit value
albums["evermore"] = 2020
print(albums)

# Print values and keys
for x, y in zip(albums.keys(), albums.values()):
    print(f"{x} was released in {y}.")