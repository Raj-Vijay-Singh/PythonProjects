import random
field = {"A": None, "B": None, "C": None}
elements = ["❤","💥"]

for key in minefield:
    field[key] = random.choice(elements)

for key