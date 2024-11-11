class Vehicle:
    def __init__(self, brand, color, doors):
        self.brand = brand
        self.doors = doors
        self.color = color

    def drive(self):
        print(f"It is being driven.")

    def rest(self):
        print(f"It is not moving.")

class Bus(Vehicle):
    def details(self):
        print(f"Brand: {self.brand}\nColor: {self.color}\nDoors: {self.doors}")

bus1 = Bus("Volvo", "Yellow", 1)
bus2 = Bus("Marcopolo", "White", 4)
bus1.details()
print()
bus2.details()
