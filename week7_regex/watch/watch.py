import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if link := re.search(r".*(https?://(www.)?)(.*)/embed/(.*)\">.*",s):
        s = f"https://youtu.be/{link.group(4)}"
        return s
    else:
        return "None"


if __name__ == "__main__":
    main()
