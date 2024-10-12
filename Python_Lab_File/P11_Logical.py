age = int(input("Enter your age: "))
marks = int(input("Enter the marks you got on entrance test (out of 100): "))

if (age >= 18 and age <= 25) and marks >= 90:
    print("You are eligible for highest scholarship.")
elif (age >= 25 and age <= 35) and marks >= 80:
    print("You are eligible for second highest scholarship.")
elif marks >= 70 and (age >= 18 and age <= 25):
    print("You are eligible for third highest scholarship.")
elif not (age>18 and marks > 70):
    print("You are ineligible for any scholarship.")
else:
    print("You are eligible for lowest scholarship.")


