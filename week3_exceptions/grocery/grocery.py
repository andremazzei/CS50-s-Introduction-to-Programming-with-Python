"""
Suppose that you’re in the habit of making a list of items you need from the grocery store.

In a file called grocery.py, implement a program that prompts the user for items, one per line,
until the user inputs control-d (which is a common way of ending one’s input to a program). Then
output the user’s grocery list in all uppercase, sorted alphabetically by item, prefixing each
line with the number of times the user inputted that item. No need to pluralize the items. Treat
the user’s input case-insensitively.
"""


grocery = {}

while True:
    try:
        i = input("").upper()
        if i in grocery:
            grocery[i] += 1
        else:
            grocery[i] = 1

    except EOFError:
        for i in sorted(grocery):
            print(grocery[i], i)
        break



