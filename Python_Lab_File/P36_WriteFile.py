f = open("TestFile.txt", "w")
f.write("It turned into something bigger\nSomewhere in the haze, got a sense I'd been betrayed.\n")
f.writelines(["Your finger on my hair pin trigger\n", "Soldier down on that icy ground\n", "Looked up at me with honor and truth.\n"])
f.close()

x = open("TestFile.txt", "r")
print(x.read())
x.close()