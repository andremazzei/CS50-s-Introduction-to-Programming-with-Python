import sys


def main():
    file_name = argv_input()
    number_of_lines = check_file(file_name)
    print(number_of_lines)

# Define argv if input is valid or not.
def argv_input():
    input = sys.argv
    if len(input) < 2:
        sys.exit("Too few command-line arguments")
    elif len(input) > 2:
        sys.exit("Too many command-line arguments")
    elif input[1].endswith(".py") == False:
        sys.exit("Not a Python file")
    else:
        return input[1]

# Open file, check if it exists and check numbers of lines.
def check_file(file_name):
    try:
        with open(file_name) as file:
            number_of_lines = 0
            for line in file:
                if line.lstrip().startswith("# ") == True:
                    continue
                if line.isspace() == True:
                    continue
                else:
                    number_of_lines += 1

        return number_of_lines
    except FileNotFoundError:
        sys.exit("File does not exist")



if __name__ == "__main__":
    main()
