"""A number-guessing game."""

import random

# Display player greeting
print("Greetings, welcome to the Guessing Game!")

# Asks for the user’s name
player_name = input("What is your name? ")

# Get random number
print(f"{player_name}, I'm thinking of a number between 1 and 100. Try to guess the number.")

secret_number = random.randint(1, 101)

# Prompt player to guess a number
guess_number = int(input("Guess a number between 1 and 100: "))


# Cycles through until the user guesses the right number

# Ends when the user guesses the right number and displays the number of guesses that the user made


