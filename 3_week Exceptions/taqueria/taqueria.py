def main():
    sum_of_items = 0
    while True:
        try:
            user_input = input("Item: ").title()
            if user_input in menu:
                sum_of_items += menu[user_input]
                print(f"${sum_of_items:.2f}")
        except EOFError:
            break
        except KeyboardInterrupt:
            break

menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

if __name__ == "__main__":
    main()