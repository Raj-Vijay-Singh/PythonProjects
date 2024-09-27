sen = input("Enter a sentence or more: ")
words = sen.split()
sword = words[0]
swordlist = []

for word in words:
    if word == sword:
        continue
    elif len(word) < len(sword):
        sword = word

for word in words:
    if word == sword:
        continue
    if len(word) == len(sword):
        swordlist.append(word)

swordlist.append(sword)

if len(swordlist) == 1:
    print("The shortest word here is: ")
elif len(swordlist) > 1:
    print("The shortest words here are: ")

for i in swordlist:
    print(i)