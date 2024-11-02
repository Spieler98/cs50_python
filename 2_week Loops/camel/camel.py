def main():
    camelCase = input("camelCase: ")
    input_list = []
    for i in camelCase:
        input_list.append(i)
        if i.isupper():
            input_list.insert(-1, "_")

    input_string = "".join(input_list).lower()

    print("snake_case:", input_string)
    
if __name__ == "__main__":
    main()