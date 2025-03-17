import random

def welcome():
    print("Welcome to the 'Guess Your Number' challenge!\n")
    print("Rules:")
    print("- Guess a number between 1 and 100.")
    print("- You'll get a certain number of chances based on the difficulty level you select.\n")

def guess_num():
    return random.randint(1, 100)

def level_select():
    levels = [10, 5, 3]
    print("Select a difficulty level:")
    print("1. Easy - 10 chances")
    print("2. Medium - 5 chances")
    print("3. Hard - 3 chances")

    while True:
        try:
            cn = int(input("\nEnter your choice (1, 2, or 3): "))
            if cn in (1, 2, 3):
                chances = levels[cn - 1]
                print(f"\nYou selected difficulty {cn}. You have {chances} chances. Good luck!\n")
                return chances
            else:
                print("Invalid input. Please enter 1, 2, or 3.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def game_play(chances, x):
    while chances > 0:
        try:
            print(f"(Chances left: {chances})")
            gs = input("Enter your guess: ").strip()

            if not gs:
                print("Invalid input! Please enter a number between 1 and 100.\n")
                continue

            gs = int(gs)

            # Validate the guess range
            if gs < 1 or gs > 100:
                print("Invalid guess! Please enter a number between 1 and 100.\n")
                continue

            # Provide feedback based on the guess
            if gs < x:
                print("Higher your guess! Try again.\n")
            elif gs > x:
                print("Lower your guess! Try again.\n")
            else:
                print(f"Congrats! Your guess is correct. The number was {x}.\n")
                break

            chances -= 1  # Deduct a chance after every incorrect guess

        except ValueError:
            print("Invalid input. Please enter a valid number.\n")

    if chances == 0:
        print(f"Out of chances! The correct number was {x}. Better luck next time!\n")

    # Replay option
    play_again = input("Do you want to play again? (yes/no): ").strip().lower()
    if play_again != "yes":
        print("Thanks for playing! Goodbye!")
        return False
    return True

# Main function to run the game
def playguess():
    while True:  # Game loop for replay
        welcome()  # Display the welcome message
        
        # Get the number of chances based on difficulty level
        chances = level_select()

        # Generate a random number for the game
        x = guess_num()

        # Start the guessing game
        if not game_play(chances, x):
            break

if __name__ == "__main__":
    playguess()  # Start the game


'''import random

# Welcome message
def welcome():    
    print("Welcome to the 'Guess Your Number' challenge!\n")
    print("Rules:")
    print("- Guess a number between 1 and 100.")
    print("- You'll get a certain number of chances based on the difficulty level you select.\n")

def guess_num():
    x = random.randint(1, 100)
    print("I have selected a number between 1 and 100. Try to guess it!\n")

def level_select():
    levels = [10, 5, 3]

    print("Select a difficulty level:")
    print("1. Easy - 10 chances")
    print("2. Medium - 5 chances")
    print("3. Hard - 3 chances")

    while True:
            try:
                cn = int(input("\nEnter your choice (1, 2, or 3): "))
                if cn in (1, 2, 3):
                    chances = levels[cn - 1]
                    print(f"\nYou selected difficulty {cn}. You have {chances} chances. Good luck!\n")
                    break
                else:
                    print("Invalid input. Please enter 1, 2, or 3.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

def game_play():
    while chances > 0:
            try:
                print(f"(Chances left: {chances})")
                gs = input("Enter your guess: ").strip()

                # Check for empty input
                if not gs:
                    print("Invalid input! Please enter a number between 1 and 100.\n")
                    continue

                gs = int(gs)

                # Validate the guess range
                if gs < 1 or gs > 100:
                    print("Invalid guess! Please enter a number between 1 and 100.\n")
                    continue

                # Provide feedback based on the guess
                if gs < x:
                    print("Lower guess! Try again.\n")
                elif gs > x:
                    print("Higher guess! Try again.\n")
                else:
                    print(f"Congrats! Your guess is correct. The number was {x}.\n")
                    break

                chances -= 1  # Deduct a chance after every incorrect guess

            except ValueError:
                print("Invalid input. Please enter a valid number.\n")

    if chances == 0:
            print(f"Out of chances! The correct number was {x}. Better luck next time!\n")

    # Replay option
    play_again = input("Do you want to play again? (yes/no): ").strip().lower()
    if play_again != "yes":
        print("Thanks for playing! Goodbye!")
        break


def playguess():
    while True:  # Game loop for replay
        # Levels and corresponding chances
        level_select()

        # Random number generation for the game
        guess_num()

        # Guessing loop
        def game_play():

if __name__=="__main__":
    welcome()'''