import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    s = re.search(r"(?:https?:\/\/)?(?:www\.)?youtube.com\/embed\/([a-zA-Z\d]*)\/?", s)
    return f"youtu.be/{s.group(1)}"



if __name__ == "__main__":
    main()