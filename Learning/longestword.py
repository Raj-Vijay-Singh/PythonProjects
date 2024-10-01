sen = input("Enter your sentence: ")
words = sen.split()
lword = words[0]
lwordlist = []

for w in words:
    if w == lword:
        continue
    if len(w) > len(lword):
        continue

for w in words:
    if w == lword:
        continue

    if len(w) == len(lword):
        lwordlist.append(w)

lwordlist.append(lword)

print("The longest words are: " if len(lwordlist) > 1 else "The longest word is: ")

prit
for i in lwordlist:
    print(i)

