with open("C:/Users/Admin/PycharmProjects/Learning/text files/test.txt","r") as test:
    lines = test.readlines()
    lanimals = lines[0]
    wanimals = lines[1]
    aerial_animals = lines[2].split()
print(aerial_animals)