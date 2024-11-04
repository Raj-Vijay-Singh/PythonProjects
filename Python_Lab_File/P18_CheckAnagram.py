word1 = input("Enter the first word: ").lower()
word2 = input("Enter the second word: ").lower()
anagram = True

for i in word1:
    if word1.count(i) != word2.count(i):
        anagram = False
        break
for j in word2:
    if word2.count(j) != word2.count(j):
        anagram = False
        break

if anagram == False:
    print("Given words are not anagrams.")
elif anagram == True:
    print("Given words are anagrams.")
else:
    print("You encountered an error!")