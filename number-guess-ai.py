def number_guessing_ai():
    print("Think of a number between 1 and 100.")
    print("I will try to guess it!")
    low = 1
    high = 100
    tries = 0
    while True:
        if low > high:
            print("Wait, you might have given contradictory answers! Let's restart.")
            low = 1
            high = 100
            tries = 0
            print("\nThink of a number between 1 and 100 again.")
            continue
        guess = (low + high) // 2
        tries += 1
        print(f"\nMy guess is {guess}.")
        reply = input("Is your number 'higher', 'lower', or 'correct'? ").strip().lower()
        if reply == "correct":
            print(f"\nYay! I guessed your number {guess} in {tries} tries!")
            break
        elif reply == "higher":
            low = guess + 1
        elif reply == "lower":
            high = guess - 1
        else:
            print("Invalid input. Please type exactly: 'higher', 'lower', or 'correct'.")
number_guessing_ai()
