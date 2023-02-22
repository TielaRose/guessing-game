"""A number-guessing game."""
import random
from termcolor import cprint


def get_name():
    """Ask for and return user's name"""
    print("Howdy, what's your name?")
    name = input("(type in your name) ").title().rstrip()
    return name


def print_guesses(lst, answer):
    """Prints user's guesses in color"""
    lst.sort()

    print("Your guesses:")

    for num in lst:
        if num < answer:
            cprint(num, "green", end="")
            print(" ", end="")
        elif num > answer:
            cprint(num, "red", end="")
            print(" ", end="")
    print("")


def ask_for_guesses(name):
    random_number = random.choice(range(1, 101))
    current_guess = 0
    num_tries = 0
    guesses = []

    while random_number != current_guess:
        print()
        if len(guesses) > 0:
            print_guesses(guesses, random_number)
            print()
        raw_guess = input("Your guess? ")

        try:
            current_guess = int(raw_guess)
        except:
            print("Guesses must be an integer")
            continue

        if current_guess < 1 or current_guess > 100:
            print("Guesses must be between 1 and 100, inclusive")
            continue

        guesses.append(current_guess)
        guesses.sort()
        num_tries += 1
        if current_guess < random_number:
            print()
            cprint("Your guess is too low, try again!", "green")
        elif current_guess > random_number:
            print()
            cprint("Your guess is too high, try again!", "red")
        else:
            break
    print()
    cprint(
        f"Well done, {name}! You found my number in {num_tries} tries!", "blue")


def play_game():
    name = get_name()

    print(f"{name}, I'm thinking of a number between 1 and 100.")
    print("Try to guess my number.")

    ask_for_guesses(name)


play_game()
