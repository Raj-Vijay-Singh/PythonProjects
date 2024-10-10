import random

def game():
    spt = "-------------"
    field = {"A": None, "B": None, "C": None, "D": None, "E": None,
             "F": None, "G": None, "H": None, "I": None, "J": None,
             "K": None, "L": None, "M": None, "N": None, "O": None,
             "P": None, "Q": None, "R": None, "S": None, "T": None,
             "U": None, "V": None, "W": None, "X": None, "Y": None}

    elements = ("❤","💥")
    hearts = 10
    liveset = {'1': 15, '2': 12, '3': 9, '4': 6, '5': 3}

    print(f"{spt}\nTHE MINEFIELD\n"
          f"Inspect letters to find the hearts. You lose a life if you find a mine instead. "
          f"Find all 10 hearts to win, lose all lives to lose.\n{spt}")
    choice = (input(f"Choose your difficulty. Enter:\n"
                    f"1 for Easy\n"
                    f"2 for Normal\n"
                    f"3 for Hard\n"
                    f"4 for Very Hard\n"
                    f"5 for Impossible\n{spt}\n"
                    f"Enter (1, 2, 3, 4 or 5): "))

    while (choice not in liveset) and (choice != "1989"):
        print(f"Enter 1, 2, 3, 4 or 5 ONLY.\n{spt}")
        choice = (input(f"Choose your difficulty. Enter:\n"
                    f"1 for Easy\n"
                    f"2 for Normal\n"
                    f"3 for Hard\n"
                    f"4 for Very Hard\n"
                    f"5 for Impossible\n{spt}\n"
                    f"Enter (1, 2, 3, 4 or 5): "))

    if choice == "1989":
        lives = 99
    else:
        lives = liveset[choice]

    guesses = []

    values = [elements[0]] * hearts + [elements[1]] * (len(field)-hearts)
    random.shuffle(values)

    for key, value in zip(field, values):
        field[key] = value

    #DISABLE BEFORE RUNNING
    # count = 0
    # for value in field.values():
    #     count += 1
    #     print(f"{value:<5}", end=" ")
    #     if count % 5 == 0:
    #         print()
    # print(spt)
    # DISABLE BEFORE RUNNING

    while lives > 0 and hearts > 0:
        print(f"{spt}\nYOUR FIELD: ")
        count = 0
        for key in field:
            count += 1
            if key in guesses:
                print(f"{field[key]:<5}", end = " ")
            else:
                print(f"{key:<5}", end = " ")
            if count%5 == 0:
                print()
        print(f"You have {lives} {'lives' if lives > 1 else 'life'}.")
        print(spt)

        guess = input("Enter one character to inspect (A-Y): ").upper()

        if guess == "ADMINWIN":
            hearts = 0
            break

        if guess == "ADMINLOSE":
            lives = 0
            break

        if guess in guesses:
            print("You already guessed this character! Idiot.")
            continue

        if guess not in field:
            print("Enter only one character (A-Y).")
            continue

        guesses.append(guess)

        if field[guess] == elements[0]:
            hearts -= 1
            print("\nYou found a heart!")

        if field[guess] == elements[1]:
            lives -= 1
            if lives > 0:
                print(f"\nYou found a mine. You have {lives} {'lives' if (lives > 1) else 'life'} now.")

    if lives == 0:
        print("You lost all your lives. Game over!")
        print(f"{spt}\nMINEFIELD: ")
        count = 0
        for value in field.values():
            count += 1
            print(f"{value:<5}", end=" ")
            if count % 5 == 0:
                print()
        print(f"{spt}\nYOUR FIELD: ")
        for key in field:
            count += 1
            if key in guesses:
                print(f"{field[key]:<5}", end=" ")
            else:
                print(f"{key:<5}", end=" ")
            if count % 5 == 0:
                print()
        print(spt)

    if hearts == 0:
        print(f"{spt}\nYou found all the hearts! Congrats!\n{spt}")

    if input("Enter 'Yes' to play again: ").upper() == "YES":
        game()

game()