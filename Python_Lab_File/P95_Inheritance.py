class Employee:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def alive(self):
        print(f"This employee is alive.")

    def present(self):
        print(f"This employee is present")

class Teacher(Employee):
    def __init__(self, name, age, gender, subject):
        super().__init__(name, age, gender)
        self.subject = subject

    def teach(self):
        print(f"This teacher is teaching {self.subject}.")

class Janitor(Employee):
    def __init__(self, name, age, gender, area):
        super().__init__(name, age, gender)
        self.area = area

    def clean(self):
        print(f"This janitor is cleaning the {self.area}.")

t1 = Teacher("Girish", 32, "Male", "English")
t2 = Teacher("Vaani", 27, "Female", "Art")
j1 = Janitor("Mukesh", 48, "Male", "Library")
j2 = Janitor("Geeta", 53, "Female", "Cafeteria")

print(f"Teacher 2:\n"
      f"Name: {t2.name}\n"
      f"Age: {t2.age}\n"
      f"Gender: {t2.gender}\n"
      f"Subject: {t2.subject}")
t2.alive()
t2.teach()
print()

print(f"Janitor 1:\n"
      f"Name: {j1.name}\n"
      f"Age: {j1.age}\n"
      f"Gender: {j1.gender}\n"
      f"Cleaning Area: {j1.area}")
j1.alive()
j1.clean()
