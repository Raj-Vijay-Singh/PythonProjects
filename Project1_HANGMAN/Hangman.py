import random
def hangman():
    print("-----------------------")
    print("HANGMAN")
    print("[A game where you guess a word by guessing characters. Be careful! You can only afford 6 wrong guesses.]")
    print("-----------------------")
    with open("hangman.txt","r") as source:
        lines = source.readlines()
        lan = lines[0].split()
        wan = lines[1].split()
        aan = lines[2].split()
        flo = lines[3].split()

    answer = random.choice(lan+wan+aan+flo)
    fanswer = answer

    if fanswer in lan:
        hint = "It is a land animal."
    elif fanswer in wan:
        hint = "It is a water animal."
    elif fanswer in aan:
        hint = "It is an aerial animal."
    elif fanswer in flo:
        hint = "It is a flower."

    guesses = []
    chars = len(answer)
    count = 0
    print("THE WORD IS:\n"+("_  "* (chars-1) +"_"))
    blank = "_" * chars
    print("\nLET US BEGIN.\n")
    tries = 0
    while tries < 7:
        guess = input("Enter your guess (Enter 5 to see hint): ").upper()
        pos = answer.find(guess)

        if guess == "5":
            print(hint)
            print()

        elif len(guess) != 1 or guess.isalpha() == False:
            print("Enter ONE character from A-Z.\n")

        elif guess in guesses:
            print("You already guessed this character.\n")

        elif pos < 0:
            tries += 1
            if tries == 1:
                print("Wrong! You can only make 5 more wrong guesses.")
            if tries == 2:
                print("Wrong! You can only make 4 more wrong guesses.")
            if tries == 3:
                print("Wrong! You can only make 3 more wrong guesses.")
            if tries == 4:
                print("Wrong! You can only make 2 more wrong guesses.")
            if tries == 5:
                print("Wrong! You can only make 1 more wrong guess.")
            if tries == 6:
                print(f"You couldn't guess the word. The word was {fanswer}. Better luck next time!")
                break
            guesses.append(guess)
            print(" ")

        elif pos >= 0:
            while pos >= 0:
                answer = answer.replace(answer[pos],"_",1)     #1 means only replace one occurence. We are running a loop, hence replacing each occurence once.
                blank = blank[:pos]+guess+blank[pos +1:]     #We are basically modifying blank variable by slicing it midway and inserting the guessed char in position. We can't use replace because every char is _ and it will replace the first one always.
                pos = answer.find(guess)
                guesses.append(guess)

            for i in blank:
                print(i,end=" ")
            print("\n")
            if blank.find("_") < 0:
                print("You got it, champ! See you next time around!")
                break

    choice = input("\nType 'Yes' to play again or 'No' to quit.\nEnter: ").upper()

    while choice != "YES" and choice != "NO":
        print("\nEnter 'Yes' or 'No'.")
        print()
        choice = input("Type 'Yes' to play again or 'No' to quit.\nEnter: ").upper()

    if choice == "YES":
        hangman()
    else:
        pass

hangman()