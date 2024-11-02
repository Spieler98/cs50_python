import csv
import sys


def main():
    if validate_arguments():
        try:
            data = []
            with open(sys.argv[1]) as file:
                reader = csv.DictReader(file)
                for row in reader:
                    last, first = row["name"].split(", ")
                    row["name"] = f"{first}, {last}"
                    data.append(row)
            sorted_data = sorted(data, key=lambda row: row["name"])

            with  open(sys.argv[2], "w", newline="") as output:
                fieldnames = ["name", "house"]
                writer = csv.DictWriter(output, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(sorted_data)
        except FileNotFoundError:
            print("File not found")

def validate_arguments():
    if len(sys.argv) == 3:
        if sys.argv[1].endswith(".csv") and sys.argv[2].endswith(".csv"):
            return True
        else:
            print("File not csv")
    elif len(sys.argv) < 3:
        print("Too few arguments")
    else:
        print("Too many arguments")

if __name__ == "__main__":
    main()