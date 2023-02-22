"""A number-guessing game."""

# ask user for their name
# computer will pick a random number between 1 and 100
# user will guess a number; computer will say, "too low" or "too high"
# when user guesses correctly, display number of guesses


def greet_player():
    print("Howdy, what's your name?")
    name = input("(type in your name) ").title().rstrip()
    print(f"{name}, I'm thinking of a number between 1 and 100.")
    print("Try to guess my number.")


greet_player()
