countries = {
    "Nepal": "Kathmandu",
    "France": "Paris",
    "Italy": "Rome",
    "UK": "London"
}

country = input("Enter the name of a country capital: ").capitalize()

if country in countries.values():
    print(f"{country} is present in the dictionary.")
else:
    print(f"{country} is not present in the dictionary.")