"""A number-guessing game."""
import random

# ask user for their name
# computer will pick a random number between 1 and 100
# user will guess a number; computer will say, "too low" or "too high"
# when user guesses correctly, display number of guesses

name = ""


def greet_player():
    print("Howdy, what's your name?")
    name = input("(type in your name) ").title().rstrip()
    print(f"{name}, I'm thinking of a number between 1 and 100.")
    print("Try to guess my number.")


def ask_for_guesses(name):
    random_number = random.choice(range(1, 101))
    user_guess = 0
    num_tries = 0
    while random_number != user_guess:
        user_guess = int(input("Your guess? "))
        num_tries += 1
        if user_guess < random_number:
            print("Your guess is too low, try again!")
        elif user_guess > random_number:
            print("Your guess is too high, try again!")
        else:
            break
    print(f"Well done, {name}! You found my number in {num_tries} tries!")


greet_player()
ask_for_guesses(name)
