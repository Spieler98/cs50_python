import sys
import random


def main():
    user_level = get_user_input("Level: ")
    random_number = generate_random_number(user_level)
    game_init(random_number)


def game_init(number):
    while True:
        guess = get_user_input("Guess: ")
        if guess == number:
            print("Just right!")
            sys.exit()
        elif guess < number:
            print("Too small")
        else:
            print("Too large!")

def generate_random_number(i):
    return random.randrange(i) + 1

def get_user_input(s):
    while True:
        try:
            user_input = int(input(s))
            return user_input
        except ValueError:
            continue
        except (KeyboardInterrupt, EOFError):
            sys.exit()


if __name__ == "__main__":
    main()