import re

def main():
    print(count(input("Text: ")))

def count(s):
    if count := re.findall(r"\bum\b", s, re.IGNORECASE):
        return len(count)
    else:
        return 0

if __name__ == "__main__":
    main()
