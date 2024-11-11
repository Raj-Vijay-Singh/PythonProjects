class Vehicle:
    def __init__(self, ms, mil):
        self.max_speed = ms
        self. mileage = mil

v1 = Vehicle(180, 100000)
v2 = Vehicle(200, 200000)

print(v1.max_speed, v1.mileage)
print(v2.max_speed, v2.mileage)
