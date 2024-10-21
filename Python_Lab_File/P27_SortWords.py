str = input("Enter some words separated by a comma (no spaces): ")
wlist = str.split(",")
wlist.sort()
print(f"{",".join(wlist)}")