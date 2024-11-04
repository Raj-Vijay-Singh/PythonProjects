import copy
import random

sep = "---------------------"
blank = "✖"

field1 = {}
for i in range(1,101):
    field1[i] = None


field2 = copy.deepcopy(field1)

ships = (("●","■","■","■","●"),
         ("●","■","■","●"),
         ("●","■","●"),
         ("●","■","●"),
         ("●","●"))

for field in [field1, field2]:
    for ship in ships:
        ind = 2
        while field[ind] != None:
            ind = random.choice(list(field.keys()))
        field[ind] = ship[0]
        dir = []
        hulim = hllim = vulim = vllim = ind
        while str(abs(hulim))[-1] != "1":
            hulim -= 1
        while str(abs(hllim))[-1] != "0":
            hllim += 1
        print(ind)

        while str(abs(vulim)) != "10" and len(str(vulim)) != 1:
            vulim -= 10
        while str(abs(vllim))[0] != "9" and len(str(vllim)) != 3:
            vllim += 10

        # Left
        if ind + (1 * len(ship)) <= hllim:
            dir.append("right")
        if ind - (1 * len(ship)) >= hulim:
            dir.append("left")
        if ind + (10* len(ship)) <= vllim:
            dir.append("down")
        if ind - (10 * len(ship)) >= vulim:
            dir.append("up")

        fix = random.choice(dir)

        for i in range(1, len(ship)):
            if fix == "up":
                ind -= 10
            if fix == "down":
                ind += 10
            if fix == "left":
                ind -= 1
            if fix == "right":
                ind += 1
            field[ind] = ship[i]

    for i in field:
        if field[i] == None:
            field[i] = "✖"

def printfield(field, guesses, player):
    print(sep)
    print(f"{player}'s field: ")
    count = 0
    for i, j in zip(field.keys(), field.values()):
        if i == 1:
            print("  ", end = "")
        if i in guesses:
            print(f"{j:<5}", end = " ")
        else:
            print(f"{i:<5}", end = " ")
        count += 1
        if count%10 == 0:
            print()
    print()

player1 = input("Enter the name of Player 1: ")
player2 = input("Enter the name of Player 2: ")
guesses1 = []
guesses2 = []
parts1 = 17
parts2 = 17
gameover = False

while not gameover:
    for guesses, player, field in zip([guesses1, guesses2], [player1, player2], [field1, field2]):
        guess = int(input("Enter the number you want to shoot (1-100): ")

        if guess1 not in field:
            print("Enter a number from 1 to 100.")
            continue

        if guess in guesses:
            print("You already shot on that tile!")
            continue

        guesses.append(guess)

        if field[guess] == blank:
            print("You hit a blank!")
        else:
            print("You hit a ship!")













