import sys
import csv


def main():
    argv_input()
    old_file = read_and_split_name(sys.argv[1])
    new_list(sys.argv[2],old_file)

# Check file name.
def argv_input():
    input = sys.argv
    if len(input) < 3:
        sys.exit("Too few command-line arguments")
    elif len(input) > 3:
        sys.exit("Too many command-line arguments")
    elif input[1].endswith(".csv") == False or input[2].endswith(".csv") == False:
        sys.exit("Not a CSV file")
    else:
        pass

# Read before.csv and output list with splited name.
def read_and_split_name(file_input) -> list:
    splits_list = []
    try:
        with open(file_input) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                last, first = row["name"].split(", ")
                splits_list.append({"first": first, "last": last, "house": row["house"]})

            return splits_list

    except FileNotFoundError:
        sys.exit(f"Could not read {file_input}")

# Save new file with three columns first, last and house.
def new_list(new_file_name, old_file:list):
    with open(new_file_name, "w") as csvfile:
        fieldnames = ["first", "last", "house"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in old_file:
            writer.writerow(row)



if __name__ == "__main__":
    main()
