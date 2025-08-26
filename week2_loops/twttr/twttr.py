"""
When texting or tweeting, it’s not uncommon to shorten words to save time or space, as by omitting vowels,
much like Twitter was originally called twttr. In a file called twttr.py, implement a program that prompts
the user for a str of text and then outputs that same text but with all vowels (A, E, I, O, and U) omitted,
whether inputted in uppercase or lowercase.
"""


def main():
    word = input("Input: ")
    vowels_remover(word)
    print()


def vowels_remover(n):
    vowels = ["a","e","i","o","u"]
    for letters in n:
        if letters.lower() in vowels:
            print("", end="")
        else:
            print(letters, end="")

main()
