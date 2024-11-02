def main():
    while True:
        try:
            x, y = input("Fraction: ").split("/")
            x, y = int(x), int(y)

            if x > y:
                continue
            
            sum_of = x/y * 100
            sum_of = round(sum_of)

            if sum_of <= 1:
                print("E")
            elif sum_of >= 99:
                print("F")
            else:
                print(sum_of,"%", sep="")

            break
        
        except ValueError:
            continue
        except ZeroDivisionError:
            continue
        except KeyboardInterrupt:
            print("Terminated by user")
            break


if __name__ == "__main__":
    main()