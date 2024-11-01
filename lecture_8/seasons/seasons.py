import sys
import re
from datetime import date

import inflect
p = inflect.engine()


def main():
    year, month, day = date_validation(input("Date of Birth: "))
    delta = date.today() - date(int(year), int(month), int(day))
    total_minutes = delta.days * 24 * 60
    print(f"{p.number_to_words(total_minutes, andword="").capitalize()} minutes")


def date_validation(birth_date):
    if re.search(r"^\d{4}-\d{2}-\d{2}$", birth_date):
        date.fromisoformat(birth_date)
        year, month, day = birth_date.split("-")
        return year, month, day

    else:
        sys.exit("Invalid date")


if __name__ == "__main__":
    main()
