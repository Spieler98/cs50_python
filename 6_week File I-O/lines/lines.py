import sys

def main():
    file_path = validate_arguments()
    print(count_lines(file_path))


def count_lines(file):
    try:
        with open(file, "r") as f:
            count = 0
            for i in f:
                if i.startswith("\n"):
                    continue
                elif i.startswith("#"):
                    continue
                else:
                    count += 1
            return count
    except FileNotFoundError:
        print("File not found")

def validate_arguments():
    if len(sys.argv) == 2:
        if sys.argv[1].endswith(".py"):
            f = sys.argv[1]
            return f
        else:
            print("Not a python file")
            sys.exit()
    elif len(sys.argv) < 2:
        print("Too few arguments")
        sys.exit()
    else:
        print("Too many argument")
        sys.exit()

if __name__ == "__main__":
    main()