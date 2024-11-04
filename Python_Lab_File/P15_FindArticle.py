pref = input("Enter a sentence or more: ").lower()
article = ["a","an","the"]
minb = float('inf')
fa = ""
words = pref.split()
for i in words:
    if i in article:
        fa = i
        break

if fa != "":
    print(f"First article to occur in the string is: {fa}")
else:
    print("There are no articles in this sentence.")