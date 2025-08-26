"""In the United States, dates are typically formatted in month-day-year order (MM/DD/YYYY), otherwise known as middle-endian order, which is arguably bad design. Dates in that format can’t be easily sorted because the date’s year comes last instead of first. Try sorting, for instance, 2/2/1800, 3/3/1900, and 1/1/2000 chronologically in any program (e.g., a spreadsheet). Dates in that format are also ambiguous. Harvard was founded on September 8, 1636, but 9/8/1636 could also be interpreted as August 9, 1636!

Fortunately, computers tend to use ISO 8601, an international standard that prescribes that dates should be formatted in year-month-day (YYYY-MM-DD) order, no matter the country, formatting years with four digits, months with two digits, and days with two digits, “padding” each with leading zeroes as needed.

In a file called outdated.py, implement a program that prompts the user for a date, anno Domini, in month-day-year order, formatted like 9/8/1636 or September 8, 1636, wherein the month in the latter might be any of the values in the list below:

[
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
]
Then output that same date in YYYY-MM-DD format. If the user’s input is not a valid date in either format, prompt the user again. Assume that every month has no more than 31 days; no need to validate whether a month has 28, 29, 30, or 31 days."""



month_names = [
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
]

def remove_date_marks(date,string):
    while True:
        date = input(string)
        try:
            if "/" in date:
                date = date.replace(" ","").split("/")
                if int(date[0]) > 0 and int(date[0]) < 13 and int(date[1]) > 0 and int(date[1]) < 32 and len(date[2]) == 4:
                    return date
            elif "," in date:
                date = date.replace(",","").split()
                if date[0] in month_names and int(date[1]) > 0 and int(date[1]) < 32 and len(date[2]) == 4:
                    if date[0].isnumeric() == False:
                        for i in range(len(month_names)):
                            if date[0] == month_names[i]:
                                date[0] = i + 1
                                return date
        except ValueError:
            pass

date = 0
month, day, year = remove_date_marks(date,"Date: ")

day = int(day)
month = int(month)
print(f"{year}-{month:02}-{day:02}")
