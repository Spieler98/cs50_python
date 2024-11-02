def main():
    user_input = input("Type: ")
    print(shorten(user_input))

def shorten(word):
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    for i in vowels:
        word = word.replace(i, "")
    return word


if __name__ == "__main__":
    main()