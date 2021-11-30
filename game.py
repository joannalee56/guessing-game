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

counter = 0
while True:
    # Prompt player to guess a number
    guess_number = int(input("Guess a number between 1 and 100: "))
    counter += 1
    if guess_number != secret_number:
        if guess_number > secret_number:
            print("Your guess is too high. Try again")
        else:
            print("Your guess is too low. Try again")
    # Ends when the user guesses the right number and displays the number of guesses that the user made
    else:
        print(f"Well done, {player_name}! You found my number in {counter} tries!")
        break

