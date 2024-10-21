emps = ["Natasha", "Bob"]
defaults = {"Class": "CSE", "Status": "Pass", "Course": "B. Tech"}
fdict = dict.fromkeys(emps, defaults)
print(fdict)
print(fdict["Bob"])