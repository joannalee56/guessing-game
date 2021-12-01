"""A number-guessing game."""

import random

# Display player greeting
print("Greetings, welcome to the Guessing Game!")

# Asks for the user’s name
player_name = input("What is your name? ")

# Get random number

print(f"{player_name}, I'm thinking of a number between 1 and 100. Try to guess the number.")

secret_number = random.randint(1, 101)
print(secret_number)

    # Cycles through until the user guesses the right number
play_game = True
counter = 0
scores = []
while play_game == True:
    try:
        # Prompt player to guess a number
        guess_number = int(input("Guess a number between 1 and 100: "))

        if guess_number < 1 or guess_number > 100:
            print("Out of range. Please enter a valid number between 1 and 100.")
        else:
            counter += 1
            if guess_number != secret_number:
                if guess_number > secret_number:
                    print("Your guess is too high. Try again")
                else:
                    print("Your guess is too low. Try again")
            # Ends when the user guesses the right number and displays the number of guesses that the user made
            else:
                print(f"Well done, {player_name}! You found my number in {counter} tries!")
                scores.append(counter)
                print(scores)

# This is not working, the Y/N?
                continueGame = True
                while continueGame == True:
                    play_again = input("Would you like to play again? Y/N: ")
                    if play_again == "Y" or play_again == "y":
                        play_game == True
                        continueGame == False
                        secret_number = random.randint(1, 101)
                        print(secret_number)
                        counter = 0
                    elif play_again == "N" or play_again == "n":
                        play_game == False
                        continueGame == False
                        break
                    else:
                        print("Please enter Y or N.")
                        continueGame == True
                    
    except ValueError:
        print("Oops! That was not a number. Please enter a valid number.")
