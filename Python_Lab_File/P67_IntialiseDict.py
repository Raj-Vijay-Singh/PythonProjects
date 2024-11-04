emps = ["Kelly", "Emma"]
defaults = {"Designation": "Developer", "Salary": 8000}
fdict = dict.fromkeys(emps, defaults)
print(fdict)
print(fdict["Kelly"])