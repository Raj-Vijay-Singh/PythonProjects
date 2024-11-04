countries = {
    "Nepal": "Kathmandu",
    "France": "Paris",
    "Italy": "Rome",
    "UK": "London"
}

capital = input("Enter the name of a country's capital: ").capitalize()

if capital in countries.values():
    print(f"{capital} is present in the dictionary.")
else:
    print(f"{capital} is not present in the dictionary.")