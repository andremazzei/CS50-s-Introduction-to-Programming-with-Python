import sys
import csv
from tabulate import tabulate


def main():
    file_name = argv_input()
    list = get_list(file_name)
    print(tabulate(list[1:], list[0], tablefmt="grid"))

# Check file name.
def argv_input():
    input = sys.argv
    if len(input) < 2:
        sys.exit("Too few command-line arguments")
    elif len(input) > 2:
        sys.exit("Too many command-line arguments")
    elif input[1].endswith(".csv") == False:
        sys.exit("Not a CSV file")
    else:
        return input[1]

# Read the file and return a list
def get_list(file) -> list:
    try:
        with open(file) as csvfile:
            reader = csv.reader(csvfile)
            list = []
            for row in reader:
                list.append(row)
            return list

    except FileNotFoundError:
        sys.exit("File does not exist")

if __name__ == "__main__":
    main()
