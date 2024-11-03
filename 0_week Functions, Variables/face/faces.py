def main():
    user_input = input("Input: ")
    converted_input = convert(user_input)
    print(converted_input)

def convert(user_input):
    user_input.replace(":(", "🙁").replace(":)", "🙂")

if __name__ == "__main__":
    main()
