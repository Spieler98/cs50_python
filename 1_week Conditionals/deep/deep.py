def main():
        user_input = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").lower()

        if user_input in {"42", "forty-two", "forty two"}:
            print("Yes")
        else:
            print("No")

if __name__ == "__main__":
    main()