import re

def main():
    print(convert(input("Hours: ")))

def convert(s):
    if time := re.search(r"^([0-1]?[0-9])(:[0-5][0-9])? (AM|PM) to ([0-1]?[0-9])(:[0-5][0-9])? (AM|PM)$",s):
        h1 = int(time.group(1))
        m1 = time.group(2)
        am_pm_1 = time.group(3)
        h2 = int(time.group(4))
        m2 = time.group(5)
        am_pm_2 = time.group(6)
        # Convert to 24h
        if am_pm_1 == "PM" and h1 != 12:
            h1 = h1 + 12
        if am_pm_2 == "PM"and h2 != 12:
            h2 = h2 + 12
        if am_pm_1 == "AM" and h1 == 12:
            h1 = 0
        if am_pm_2 == "AM" and h2 == 12:
            h2 = 0
        # Check if there are minutes
        if m1 == None:
            m1 = ":00"
        if m2 == None:
            m2 = ":00"
        return f"{h1:02}{m1} to {h2:02}{m2}"
    else:
        raise ValueError

if __name__ == "__main__":
    main()
