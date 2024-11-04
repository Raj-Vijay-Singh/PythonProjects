str = input("Enter some words separated by a comma (no spaces):\n")
wlist = str.split(",")
wlist.sort()
print(f"The words sorted in alphabetical order:\n{", ".join(wlist)}")