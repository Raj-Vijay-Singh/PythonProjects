sen = input("Enter a sentence or more: ")
word = input("Enter the string you want to find last occurrence of: ")
count = sen.count(word)
start = -1

for i in range (1,count+1):
    start = sen.find(word,start+1)

print(start)



