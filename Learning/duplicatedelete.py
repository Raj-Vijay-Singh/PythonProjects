a = "Cha hall is interesting"
ra = a[::-1]
for i in a:
    if i == " ":
        continue
    if ra.count(i) > 1:
        ra = ra.replace(i,"",a.count(i)-1)

print(ra[::-1])