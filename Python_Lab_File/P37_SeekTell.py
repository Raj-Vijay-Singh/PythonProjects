f = open("Seek&TellExp.txt", "r")

# Finding cursor position using tell()
print(f.tell())
print(f.readline())

# Finding new cursor position
print(f.tell())

#Moving to new position
f.seek(67)
print(f.readline())
print(f.read())