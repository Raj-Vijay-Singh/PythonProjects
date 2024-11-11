data = {
    "Harsh": {
        "Physics": 90,
        "Chemistry": 94,
        "Maths": 2,
    },
    "Vineet": {
        "PPS":
            {
                "Theory": 87,
                "Practical": 100
            },
        "History": 20
    },
    "Geeta": {
        "Maths": 76,
        "Biology": 87,
        "English": 50
    }
}

data["Vineet"]["PPS"]["Written"] = data["Vineet"]["PPS"].pop("Theory")

for x, y in zip(data, data.values()):
    print(f"{x}: {y}")