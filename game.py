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
            cprint(num, "magenta", end="")
            print(" ", end="")
    print("")


def get_rand_num():
    """Asks user to input a lower and upper bound for the range, returns a tuple (lower_bound, upper_bound, random num in range)"""

    # ask user to input lower bound
    while True:
        print("Enter the lowest number I should pick:")
        lower_bound = input("> ")

        # validate input is an integer
        try:
            lower_bound = int(lower_bound)
            break
        except:
            cprint("Input must be a number. Try again", "red")
            continue

    print()

    # ask user to input upper bound
    while True:
        print("Enter the highest number I should pick:")
        upper_bound = input("> ")

        # validate input is an integer
        try:
            upper_bound = int(upper_bound)
        except:
            cprint("Input must be a number. Try again", "red")
            continue

        # validate upper bound is higher than lower bound
        if upper_bound > lower_bound:
            break
        else:
            cprint(f"Enter a number higher than {lower_bound}", "red")

    print()
    print(
        f"Great! I am thinking of a number between {lower_bound} and {upper_bound}")

    # generate a random number in the range given
    answer = random.choice(range(lower_bound, (upper_bound + 1)))

    return (lower_bound, upper_bound, answer)


def ask_for_guesses(name, answer_tup):
    current_guess = 0
    num_tries = 0
    guesses = []
    lower_bound = answer_tup[0]
    upper_bound = answer_tup[1]
    answer = answer_tup[2]

    while answer != current_guess:
        print()
        if len(guesses) > 0:
            print_guesses(guesses, answer)
            print()
        print(f"Guess a number between {lower_bound} and {upper_bound}")
        raw_guess = input("> ")

        try:
            current_guess = int(raw_guess)
        except:
            cprint("Guesses must be an integer", "red")
            continue

        if current_guess < lower_bound or current_guess > upper_bound:
            cprint(
                f"Guesses must be between {lower_bound} and {upper_bound}, inclusive", "red")
            continue

        guesses.append(current_guess)
        guesses.sort()
        num_tries += 1
        if current_guess < answer:
            print()
            cprint("Your guess is too low, try again!", "green")
        elif current_guess > answer:
            print()
            cprint("Your guess is too high, try again!", "magenta")
        else:
            break
    print()
    cprint(
        f"Well done, {name}! You found my number in {num_tries} tries!", "green")


def play_game():
    name = get_name()
    print()

    print(f"Hi {name}!")
    answer_tup = get_rand_num()

    ask_for_guesses(name, answer_tup)


play_game()
