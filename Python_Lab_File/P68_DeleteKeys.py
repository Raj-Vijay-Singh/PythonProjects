movies = {
    "Ready Or Not": 2019,
    "The Substance": 2024,
    "Alien": 1979,
    "Barbarian": 2022,
    "[Rec]": 2007
}

rlist = ["Barbarian", "Alien"]

for item in rlist:
    movies.pop(item)

print(f"Dictionary after keys deleted:\n{movies}")