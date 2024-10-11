height = float(input("Enter your height in meters: "))
weight = float(input("Enter your weight in kg: "))

BMI = round(weight / (height * height), 2)

status = ""
if BMI <= 18.4:
    status = "Underweight"
elif 24.9 >= BMI > 18.4:
    status = "Normal"
elif 40 > BMI > 24.9:
    status = "Overweight"
elif BMI >= 40:
    status = "Obese"
else:
    status = "Invalid"

print(f"Your BMI is {BMI}: {status}")