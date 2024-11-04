s1 = int(input("Enter the first side of the triangle: "))
s2 = int(input("Enter the second side of the triangle: "))
s3 = int(input("Enter the third side of the triangle: "))

slist = [s1, s2, s3]
slist.remove(max(slist))

if ((slist[0]**2) + (slist[1]**2)) == max(s1, s2, s3)**2:
    print("It is a right angled triangle.")
else:
    print("It is not a right angled triangle.")
