import random

dice_art = {
    1: ("┌───────────┐",
         "│                        │",
         "│          ●           │",
         "│                        │",
         "└───────────┘"),
    2: ("┌───────────┐",
         "│   ●                  │",
         "│                        │",
         "│                  ●   │",
         "└───────────┘"),
    3: ("┌───────────┐",
         "│   ●                  │",
         "│           ●          │",
         "│                  ●   │",
         "└───────────┘"),
    4: ("┌───────────┐",
         "│   ●           ●   │",
         "│                        │",
         "│   ●           ●   │",
         "└───────────┘"),
    5: ("┌───────────┐",
         "│   ●           ●   │",
         "│          ●          │",
         "│   ●           ●   │",
         "└───────────┘"),
    6: ("┌───────────┐",
     "│   ●           ●   │",
     "│   ●           ●   │",
     "│   ●           ●   │",
     "└───────────┘")
}

dice = []
total = 0
num_of_dice = int(input("How many dice?: "))

for die in range(num_of_dice):
    dice.append(random.randint(1, 6))

# for die in dice:
#     for line in dice_art[die]:
#         print(line)

for i in range(5):
    for die in dice:
        print(dice_art[die][i],end=" ")
    print()