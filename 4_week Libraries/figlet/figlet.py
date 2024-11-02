import sys
import secrets
from pyfiglet import Figlet


def main():
    if validate_arguments():
        user_input = get_user_input()
        print(Figlet(font=sys.argv[2]).renderText(user_input))
    else:
        user_input = get_user_input()
        random_font = secrets.choice(Figlet().getFonts())
        print(Figlet(font=random_font).renderText(user_input))


def validate_arguments():
    if len(sys.argv) == 1:
        return False
    elif len(sys.argv) == 3:
        if sys.argv[1] == "-f" or sys.argv[1] == "--font":
            font_list = Figlet().getFonts()
            if sys.argv[2] in font_list:
                return True
            else:
                invalid_usage_exit()
        else:
            invalid_usage_exit()
    else:
        invalid_usage_exit()


def invalid_usage_exit():
    print("Invalid usage")
    sys.exit()

def get_user_input():
    try:
        return input("Input: ")
    except KeyboardInterrupt:
        print("Terminated by user")
        sys.exit()


if __name__ == "__main__":
    main()