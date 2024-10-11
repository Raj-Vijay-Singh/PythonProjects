# Empty tuple
t1 = ()
print(f"Empty tuple: {t1}")

# Tuple with elements
t2 = (1, 2, 3)
print(f"Tuple with elements: {t2}")

# Tuple with mixed elements
t3 = (1, 98.76, "Reputation", True)
print(f"Tuple with mixed elements: {t3}")

# Nested tuple
t4 = (20, 30, (500, 600, 900), "Glassware", "Florist")
print(f"Nested tuple: {t4}")

# Tuple packing & unpacking
t5 = "Red", "Blue", "Green"
print(f"Packed tuple: {t5}")
x, y, z = t5
print(f"Unpacked tuple: {x}, {y}, {z}")