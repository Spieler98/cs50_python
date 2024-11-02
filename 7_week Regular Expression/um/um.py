import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    counter = 0
    if match:= re.findall(r"\bum\b", s, flags=re.IGNORECASE):
        for _ in match:
            counter += 1
    return counter

if __name__ == "__main__":
    main()