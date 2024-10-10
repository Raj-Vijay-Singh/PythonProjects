# Creating a file
#f = open("testfile.txt","x")

# Writing in a file
def read_file(a):
    x = open(a)
    print(x.read())

read_file("testfile.txt")