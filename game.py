"""A number-guessing game."""
import random

# ask user for their name
# computer will pick a random number between 1 and 100
# user will guess a number; computer will say, "too low" or "too high"
# when user guesses correctly, display number of guesses


def get_name():
    print("Howdy, what's your name?")
    name = input("(type in your name) ").title().rstrip()
    return name


def ask_for_guesses(name):
    random_number = random.choice(range(1, 101))
    current_guess = 0
    num_tries = 0
    guesses = []

    while random_number != current_guess:
        print()
        if len(guesses) > 0:
            print("So far you have guessed: ", guesses)
            print()
        current_guess = int(input("Your guess? "))
        guesses.append(current_guess)
        num_tries += 1
        if current_guess < random_number:
            print()
            print("Your guess is too low, try again!")
        elif current_guess > random_number:
            print()
            print("Your guess is too high, try again!")
        else:
            break
    print(f"Well done, {name}! You found my number in {num_tries} tries!")


def play_game():
    name = get_name()

    print(f"{name}, I'm thinking of a number between 1 and 100.")
    print("Try to guess my number.")

    ask_for_guesses(name)


play_game()
