from validator_collection import checkers

def main():
    print(check_email(input("What's your email address? ")))



def check_email(e):
    result = checkers.is_email(e)
    if result == True:
        return "Valid"
    else:
        return "Invalid"


if __name__ == "__main__":
    main()
