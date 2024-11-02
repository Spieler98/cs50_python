import sys
import csv
from tabulate import tabulate


if len(sys.argv) == 2:
    if sys.argv[1].endswith(".csv"):
        try:
            with open(sys.argv[1]) as file:
                reader = csv.reader(file)
                print(tabulate(reader, headers="firstrow", tablefmt="grid"))
        except FileNotFoundError:
            print("File does not exist")
    else:
        print("File not csv")
elif len(sys.argv) < 2:
    print("Too few arguments")
else:
    print("Too many arguments")