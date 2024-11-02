import sys


def main():
    try:
        x, y = input("Fraction: ").split("/")
        x, y = int(x), int(y)
        percentage = convert(x, y)
        print(gauge(percentage), "%", sep="")
    except ValueError:
        pass
    except (KeyboardInterrupt,EOFError):
        print("Terminated by user")
        sys.exit()

def convert(x, y):
    sum_of = x/y * 100
    return sum_of

def gauge(sum_of):
    if sum_of <= 1:
        return "E"
    elif sum_of >= 99:
        return "F"
    else:
        return str(f"{sum_of:.0f}")


if __name__ == "__main__":
    main()