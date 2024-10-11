import random


def hangman():
    print("-----------------------")
    print("HANGMAN")
    print("[A game where you guess a word by guessing characters. Be careful! You can only afford 6 wrong guesses.]")
    print("-----------------------")

    with open("hangman.txt", "r") as source:
        lines = source.readlines()
        lan = lines[0].split(", ")
        wan = lines[1].split(", ")
        aan = lines[2].split(", ")
        flo = lines[3].split(", ")

    answer = random.choice(lan+wan+aan+flo)

    hint = "Something went wrong. Hint could not be generated."

    if answer in lan:
        hint = "It is a land animal."
    elif answer in wan:
        hint = "It is a water animal."
    elif answer in aan:
        hint = "It is an aerial animal."
    elif answer in flo:
        hint = "It is a flower."

    answer = answer.upper()

    guesses = []
    chars = len(answer)
    print("THE WORD IS:\n"+("_  " * chars))
    blank = "_" * chars
    print("\nLET US BEGIN.\n")
    tries = 0
    while tries < 6:
        guess = input("Enter your guess (Enter 5 to see hint): ").upper()

        if guess == "5":
            print(hint)
            print()
            continue

        if len(guess) != 1 or guess.isalpha() is False:
            print("Enter ONE character from A-Z.\n")
            continue

        if guess in guesses:
            print("You already guessed this character.\n")
            continue

        guesses.append(guess)

        if guess not in answer:
            tries += 1
            if tries < 6:
                print(f"Wrong! You can only make {6-tries} more wrong guess{'es' if (6-tries) > 1 else ''}.\n")

        else:
            blank = ''.join([guess if answer[i] == guess else blank[i] for i in range(chars)])
            print(" ".join(blank)+"\n")

        if "_" not in blank:
            print("You got it! Well done!\n")
            break
        else:
            if tries == 6:
                print(f"You were unable to guess the word. The word was {answer}. Better luck next time!\n")

    if input("Enter 'Yes' to play again, or anything else to exit: ").upper() == "YES":
        hangman()
    else:
        print("\nThank you for playing!")


hangman()
