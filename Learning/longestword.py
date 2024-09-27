sen = input("Enter your sentence: ")
words = sen.split()
lword = ""

for w in words:
    if len(w) > len(lword):
        lword = w

print(f"The longest word is '{lword}'")


