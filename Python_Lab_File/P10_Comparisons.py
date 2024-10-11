age = int(input("Enter your age in years: "))

if age > 18:
    print("You are not eligible to enter the exam.")
elif age == 18:
    print("This is your last chance to enter the exam.")
elif 18 > age > 13:
    print("You are eligible to enter the exam.")
elif age == 13:
    print("This is your first chance to enter the exam.")
elif 13 > age > 0:
    print("You are not eligible to enter the exam.")
else:
    print("The age you entered is invalid. ")