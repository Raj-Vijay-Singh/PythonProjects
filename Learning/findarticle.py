pref = input("Enter a sentence or more: ")
article = ["a","an","the"]
minb = float('inf')
fa = ""
pref = pref.lower()
words = pref.split()
for i in article:
    if i in words:
        b = words.index(i)
        if b < minb:
            minb = b
            fa = i
if fa != "":
    print(f"First article to occur in the string is: {fa}")
else:
    print("There are no articles in this sentence.")