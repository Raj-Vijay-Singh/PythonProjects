int_num = int(input("Enter an integer: "))
print(f"{int_num} has the data type: {type(int_num)}.")

float_num = float(input("Enter a decimal number: "))
print(f"{float_num} has the data type: {type(float_num)}.")

complex_num = input("Enter a complex number (Eg. 2+5j, 7+93j, 45-2j): ").replace(" ","")
complex_num = complex(complex_num)
print(f"{complex_num} has the data type: {type(complex_num)}.")