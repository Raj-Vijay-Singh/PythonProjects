a = input("Enter a sentence or more: ")
AA = True

for i in a:
    if i == " ":
        continue
    elif i.isalpha() != True:
        AA = False

if AA:
    print("This string has alphabetical characters only.")