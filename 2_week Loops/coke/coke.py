def main():
    sum_of_input = 0
    coke = 50
    print(f"Amount Duo: {coke}c")
    while True:
        try:
            user_input = int(input("Insert Coin: "))
            if user_input in {25, 10, 5}:
                sum_of_input += user_input
                if sum_of_input >= 50:
                    print(f"Change Owed: ", abs(sum_of_input - coke), "c", sep="")
                    break
                else:
                    print(f"Amount Due: ", abs(sum_of_input - coke), "c", sep="")

        except ValueError:
            print("Input was not a number!")

if __name__ == "__main__":
    main()