f = open("TestFile.txt", "w")
f.writelines(["This is the first line.\n", "This is the second line.\n", "This is the 3rd line.\n"])
f.close()

f = open("TestFile.txt", "r")
print(f.read())
f.close()