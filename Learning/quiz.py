def quiz():
    questions = ("How many planets are there in the solar system?: ",
                "Which of the following is the fastest animal?: ",
                "What is the highest grossing horror movie franchise of all time?: ",
                "Who is the actor or actress with the most Oscars?: ")

    options = (("A. 6","B. 8","C. 7","D. 9"),
            ("A. Swordfish","B. Cheetah","C. Penegrine Falcon","D. Ostrich"),
            ("A. It","B. The Conjuring Universe","C. Saw Franchise","D. A Quiet Place Series"),
            ("A. Katherine Hephburn","B. Will Smith","C. Jamie Lee Curtis","D. Robert Downey Jr."))

    answers = ("B","C","B","A")
    pts = 0

    for index in range(0,len(questions)):
        print("---------------------")
        print(f"Question {index+1}:")
        print(questions[index])
        print("---------------------")
        for i in options[index]:
            print(i)
        print( )
        guess = input("What is your guess (A,B,C or D) ?: ").upper()
        while len(guess) != 1 or guess.isalpha() == False:
            print("Enter ONE character.")
            guess = input("What is your guess (A,B,C or D) ?: ").upper()
        if guess == answers[index]:
            print()
            print("CORRECT ANSWER!")
            pts += 1;
        elif guess != answers[index]:
            print("WRONG ANSWER!")
    print("----------------------")
    print("RESULT")
    print("----------------------")
    print(f"You got {pts} out of {len(questions)} points!")
    print("----------------------")
    pa = input("Do you want to play again? Enter 'Yes' to play again and 'No' to quit?: ")
    while not (pa.lower() == "yes" or pa.lower() == "no"):
        print("Enter Yes or No!")
        print("----------------------")
        pa = input("Do you want to play again? Enter 'Yes' to play again and 'No' to quit?: ")
    if pa.lower() == "yes":
        print("----------------")
        quiz()
    elif pa.lower() == "no":
        pass

quiz()
print("Thank you for playing!")


