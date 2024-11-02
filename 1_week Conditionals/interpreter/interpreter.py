def main():
    user_expression = input("Expression: ")
    x, y, z = user_expression.split(" ")
    x, z = float(x), float(z)
    try:
        if y in {"+", "-", "*", "/"}:
            if y == "+":
                sumof = x + z
                print(f"{sumof:.1f}")
            elif y == "-":
                sumof = x - z
                print(f"{sumof:.1f}")
            elif y == "*":
                sumof = x * z
                print(f"{sumof:.1f}")
            elif y == "/":
                sumof = x / z
                print(f"{sumof:.1f}")
        else: 
            print(f"Operator {y} not available.")
    except ZeroDivisionError:
        print("Can't divide by 0")

if __name__ == "__main__":
    main()