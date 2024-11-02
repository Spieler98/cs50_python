import random
import sys

def main():
    level = get_level()
    play(level)


def play(level):
    guess_count = 0
    for _ in range(2):
        x = generate_integer(level)
        y = generate_integer(level)
        z = x + y
        for i in range(4):
            i += 1
            if not i == 4:
                guess = get_input(f"{x} + {y} = ")
                guess_count += 1
                if guess == str(z):
                    break
                else:
                    print("EEE")
            else:
                print(f"{x} + {y} = {z}")
    print("Guesses: ", guess_count)

def get_level():
    while True:
        try:
            level = int(get_input("Level: "))
            if level in range(1, 4):
                return level
            else:
                print("Levels 1, 2 or 3")
        except ValueError:
            pass



def generate_integer(level):
    if level == 1:
        return random.randint(1, 10)
    elif level == 2:
        return random.randint(5, 20)
    elif level == 3:
        return random.randint(10, 30)


def get_input(s):
    while True:
        try:
            user_input = input(s)
            return user_input
        except (KeyboardInterrupt, EOFError):
            sys.exit()


if __name__ == "__main__":
    main()