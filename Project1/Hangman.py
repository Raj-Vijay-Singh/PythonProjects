import random
while 1 == 1:
    list = ["LILY","HIBISCUS","SUNFLOWER","JASMINE","HYACINTHUS","LILAC","TULIP","MARIGOLD","LAVENDER"]
    answer = random.choice(list)
    chars = len(answer)
    count = 0
    print("THE WORD IS:\n"+("_  "* (chars-1) +"_"))
    blank = "_" * chars
    print("\nLET US BEGIN.\n")
    tries = 1
    while tries < 7:
        guess = input("Enter your guess: ").upper()
        pos = answer.find(guess)
        if len(guess) != 1:
            print("Enter ONE character.\n")

        elif pos < 0:
            if tries == 1:
                print("Oops, you just lost your left leg!")
            if tries == 2:
                print("Ugh, there goes your right leg! Quite bloody, ain't it?")
            if tries == 3:
                print("Sorry, gotta chop off the left arm too.")
            if tries == 4:
                print("Bad luck, right arm off your body!")
            if tries == 5:
                print("Almost dead, your belly's off. Welp.")
            if tries == 6:
                print("Serving your head to someone in a platter, buddy. Better luck next time!")
                break
            tries += 1
            print(" ")
        elif pos >= 0:
            while pos >= 0:
                answer = answer.replace(answer[pos],"_",1)
                blank = blank[:pos]+guess+blank[pos +1:]
                pos = answer.find(guess)
            for i in blank:
                print(i,end=" ")
            print("\n")
            if blank.find("_") < 0:
                print("You got it, champ! See you next time around!")
                break
    choice = input("\nType 'Yes' to play again or anything else to quit: ").upper()
    if choice == "YES":
        continue
    else:
        break