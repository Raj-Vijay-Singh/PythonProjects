from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def live(self):
        pass

    @abstractmethod
    def eat(self):
        pass

class Horse(Animal):
    def live(self):
        print("A horse lives in a stable.")

    def eat(self):
        print("A horse eats grams.")

class Shark(Animal):
    def live(self):
        print("A shark lives in ocean.")

    def eat(self):
        print("A shark eats seels.")

class Flamingo(Animal):
    def live(self):
        print("A flamingo lives by river banks.")

    def eat(self):
        print("A flamingo eats fishes.")

horse = Horse()
shark = Shark()
flamingo = Flamingo()

for animal in (horse, shark, flamingo):
    animal.live()
    animal.eat()
