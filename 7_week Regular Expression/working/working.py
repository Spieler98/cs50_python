import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if s:= re.match(r"^((?:1[0-2]|0?[0-9]|0?[0-9])(?::(?:[0-5][0-9]))?) (AM|PM) to ((?:1[0-2]|0?[0-9]|0?[0-9])(?::(?:[0-5][0-9]))?) (AM|PM)$", s):
        first, first_am_pm, second, second_am_pm = s.group(1), s.group(2), s.group(3), s.group(4)
        if ":" in first:
            first = first.split(":")
        else:
            first = [first]
            first.append("00")
        if first_am_pm == "PM":
            first[0] = int(first[0]) + 12

        if ":" in second:
            second = second.split(":")
        else:
            second = [second]
            second.append("00")
        if second_am_pm == "PM":
            second[0] = int(second[0]) + 12

        if first_am_pm == "AM" and first[0] == "12":
            first[0] = 0
        if second_am_pm == "AM" and second[0] == "12":
            second[0] = 0

        return f"{first[0]}:{first[1]} to {second[0]}:{second[1]}"
    else:
        raise ValueError("Invalid format")


if __name__ == "__main__":
    main()