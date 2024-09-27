word = input("Enter your word: ")
bword = word[::-1]
if word == bword:
    print("It's a palindrome!")
else:
    print("It's not a palindrome!")
