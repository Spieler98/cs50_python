vowels_set = {"A", "E", "I", "O", "U", "a", "e", "i", "o", "u"}

def main():
    while True:
        sentence = input("Input: ")
        for i in vowels_set:
            sentence = sentence.replace(i, "")
        print(sentence)

if __name__ == "__main__":
    main()