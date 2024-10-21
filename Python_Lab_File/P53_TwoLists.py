names = ["Daksh", "Nikunj", "Harshita", "Sagar"]
markslist = [87, 23, 0, 98]

for name, marks in zip(names, markslist[::-1]):
    print(name, marks)