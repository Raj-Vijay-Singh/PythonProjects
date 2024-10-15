def read_file(file):
    f = open(file, "r")
    print(f.read())

file = input("Enter name of the file to read (with extension): ")
read_file(file)