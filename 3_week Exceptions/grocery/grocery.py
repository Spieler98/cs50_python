grocery_items = {}

def main():
    while True:
        try:
            item = input("Items: ").lower()
            if item not in grocery_items:
                grocery_items[item] = 1
            else:
                value = grocery_items.get(item)
                value += 1
                grocery_items[item] = value
        except EOFError:
            break
        except KeyboardInterrupt:
            break

    sorted_items = sorted(grocery_items.items())
    print()
    for x in sorted_items:
        print(x[1], x[0].upper())


if __name__ == "__main__":
    main()