class Dog:
    def sound(self):
        print("A dog barks.")

class Cat:
    def sound(self):
        print("A cat meows.")

class Mouse:
    def sound(self):
        print("A mouse squeaks.")

class Crow:
    def sound(self):
        print("A crow caws.")

animals = [Dog(), Cat(), Mouse(), Crow()]

for animal in animals:
    animal.sound()