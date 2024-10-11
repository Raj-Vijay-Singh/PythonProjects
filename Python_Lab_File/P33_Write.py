f = open("TestFile.txt", "w")
f.write("This is what I am going to write.\nHello! This is the output generated in my text file.")
f.close()

x = open("TestFile.txt", "r")
print(x.read())
x.close()