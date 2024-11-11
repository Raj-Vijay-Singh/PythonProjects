class Student:
    def __init__(self, name, age, gender, branch):
        self.name = name
        self.age = age
        self.gender = gender
        self.branch = branch

s1 = Student("James", 18, "Male", "AI & ML")
s2 = Student("Betty", 18, "Female", "AI & R")
s3 = Student("August", 19, "Female", "AI & DS")

for student in (s1, s2, s3):
    print(f"Name: {student.name}\n"
          f"Age: {student.age}\n"
          f"Gender: {student.gender}\n"
          f"Branch: {student.branch}\n")