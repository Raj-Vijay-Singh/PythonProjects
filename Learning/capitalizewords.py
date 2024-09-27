sen = input("Enter a sentence or more: ")
words = sen.split()

for word in words:
    word = word.capitalize()
    print(word,end=" ")