import random
import time
import copy
def setup():
    print("----------------------")
    diff = int(input("Choose your difficulty. Enter:\n1 for Easy\n2 for Normal\n3 for Hard\n4 for Extreme\nEnter (1, 2, 3 or 4): "))
    while diff not in (1,2,3,4):
        print("Enter 1, 2, 3 or 4!")
        print("----------------------")
        diff = int(input("Choose your difficulty. Enter:\n1 for Easy\n2 for Normal\n3 for Hard\n4 for Extreme\nEnter (1, 2, 3 or 4): "))
    if diff == 1:
        lives = 12
    elif diff == 2:
        lives = 9
    elif diff == 3:
        lives = 5
    elif diff == 4:
        lives = 3
    show = [["A","B","C","D","E"],["F","G","H","I","J"],["K","L","M","N","O"],["P","Q","R","S","T"],["U","V","W","X","Y"]]
    elements = ["❤","💥"]
    field = []
    heart = True

    for i in range(5):
        flist = []
        for j in range(5):
            felement = random.choice(elements)
            flist.append(felement)
        field.append(flist)

    ffield = copy.deepcopy(field) #Creating a new field for display purposes. Deep copy is used so that changes made in "field" dont affect "ffield"
    def game(guess,lives):
        ind1 = ind2 = None
        for x in range(5):
            for y in range(5):
                if show[x][y] == guess:
                    ind1 = x
                    ind2 = y
                    break

        if ind1 == None or ind2 == None:
            print("You already inspected this letter.")
            return True

        if field[ind1][ind2] == elements[0]:
            print("\nYou found a heart!")
            time.sleep(1)
            show[ind1][ind2] = elements[0]
            field[ind1][ind2] = 0
            return True

        if field[ind1][ind2] == elements[1]:
            print(f"\nYou found a mine. Ouch. You have {lives-1} lives now.")
            time.sleep(1)
            show[ind1][ind2] = elements[1]
            return False

    # DISABLE BEFORE RUNNING, ONLY FOR TESTING
    for x in range(5):
        for y in range(5):
            print(f"{field[x][y]:^3}", end=" ")
        print()
    # DISABLE BEFORE RUNNING, ONLY FOR TESTING

    while lives != 0 and heart == True:
        print("---------------------")
        for x in range(5):
            for y in range(5):
                print(f"{show[x][y]:^3}", end=" ")
            print()
        print("---------------------")
        guess = input("Which letter do you want to inspect?: ").upper()
        while guess.isalpha() == False or len(guess) != 1:
            print("Enter one character (A-Y): ")
            print("---------------------")
            guess = input("Which letter do you want to inspect?: ").upper()
        result = game(guess,lives)
        if not result:
            lives -= 1
        heart = False
        for x in range(0, 5):
            for y in range(0, 5):
                if field[x][y] == elements[0]:
                    heart = True
                    break

    if lives == 0:
        print("---------------------")
        print("YOUR FIELD: ")
        for x in range(5):
            for y in range(5):
                print(f"{show[x][y]:^3}", end=" ")
            print()
        print("---------------------")
        print("MINE FIELD: ")
        for x in range(5):
            for y in range(5):
                print(f"{ffield[x][y]:^3}", end=" ")
            print()
        print("---------------------")
        print("Game over. You lost.")

    if heart == False:
        print("---------------------")
        print("YOUR FIELD: ")
        for x in range(0, 5):
            for y in range(0, 5):
                print(f"{show[x][y]:^3}", end=" ")
            print()
        print("---------------------")
        print("MINE FIELD: ")
        for x in range(5):
            for y in range(5):
                print(f"{ffield[x][y]:^3}", end=" ")
            print()
        print("---------------------")
        print("You won!")

    if input("----------------------\nDo you want to play again? Enter 'Yes' to play again, or anything else to quit: ").upper() == "YES":
        setup()
    else:
        print("\nThank you for playing!")


setup()






