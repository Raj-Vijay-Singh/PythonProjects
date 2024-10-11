moviedata = [["Ready Or Not", 2019, "Samara Weaving"],
             ["Annabelle", 2014, "Annabelle Wallis"],
             ["Get Out", 2017, "Daniel Kaluuyya"],
             ["Countdown", 2019, "Elisabeth Lail"],
             ["Alien", 1979, "Sigourney Weaver"]]

columno = int(input("Enter the number of column to extract: "))

if columno not in (1, 2, 3):
    print("Invalid column number.")

for row in moviedata:
    print(row[columno-1])