def main():
    while True:
        user_input = input("Date: ").title()

        if user_input.startswith(months_tuple):
            try:
                date = user_input.split()
                date[1] = date[1].replace(",", "")
                date[1] = int(date[1])
                if date[1] > 31:
                    raise ValueError
                print(f"{date[2]}-{months_dict[date[0]]}-{date[1]}")
                break
            except:
                continue
        else:
            try:
                date = user_input.split("/")
                date[1] = int(date[1])
                if date[1] > 31:
                    raise ValueError
                print(f"{date[2]}-{date[0]}-{date[1]}")
                break
            except:
                continue

months_tuple = (
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
)

months_dict = {
    "January": "01",
    "February": "02",
    "March": "03",
    "April": "04",
    "May": "05",
    "June": "06",
    "July": "07",
    "August": "08",
    "September": "09",
    "October": "10",
    "November": "11",
    "December": "12"
}

if __name__ == "__main__":
    main()