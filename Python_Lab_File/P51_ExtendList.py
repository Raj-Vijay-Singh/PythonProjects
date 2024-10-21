nlist = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
sublist = ["h", "i", "j"]

nlist[2][1][2].extend(sublist)
print(f"The nested list after extending with sublist:\n{nlist}")