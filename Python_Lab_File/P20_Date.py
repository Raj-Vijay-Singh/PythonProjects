from datetime import date

tdate = date.today()

print(f"dd/mm/yy: {tdate.strftime("%d/%m/%y")}")
print(f"Textual month, day and year: {tdate.strftime("%B %d, %Y")}")
print(f"mm/dd/yy: {tdate.strftime("%m/%d/%y")}")
print(f"Month abbreviation-day-year: {tdate.strftime("%b-%d-%y")}")
