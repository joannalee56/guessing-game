"""A number-guessing game."""

import random

print("Greetings, welcome to the Guessing Game!")
player_name = input("What is your name? ")

print(f"{player_name}, I'm thinking of a number between 1 and 100. Try to guess the number.")

secret_number = random.randint(0, 101)
print(secret_number)