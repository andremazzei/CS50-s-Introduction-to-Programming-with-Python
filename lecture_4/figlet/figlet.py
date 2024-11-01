'''
FIGlet, named after Frank, Ian, and Glen’s letters, is a program from the early 1990s for making large
letters out of ordinary text, a form of ASCII art:

Among the fonts supported by FIGlet are those at figlet.org/examples.html.

FIGlet has since been ported to Python as a module called pyfiglet.

In a file called figlet.py, implement a program that:

Expects zero or two command-line arguments:
Zero if the user would like to output text in a random font.
Two if the user would like to output text in a specific font, in which case the first of the two should be
-f or --font, and the second of the two should be the name of the font.
Prompts the user for a str of text.
Outputs that text in the desired font.
If the user provides two command-line arguments and the first is not -f or --font or the second is not the
name of a font, the program should exit via sys.exit with an error message.
'''

import sys
from pyfiglet import Figlet
import random

comand_line_inputs = sys.argv[1:3]
figlet = Figlet()
fonts_list = figlet.getFonts()

# Two inputs: first -f or --font and second font name inside fonts list
if len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "Font"):
    if sys.argv[2].lower() in fonts_list:
        figlet.setFont(font=sys.argv[2].lower())
        answer = input("Input: ")
        print(figlet.renderText(answer))

# Zero imputs (RANDOM)
elif len(sys.argv) == 1:
    figlet.setFont(Font=random.choice(fonts_list))
    answer = input("Input: ")
    print(figlet.renderText(answer))

else:
    sys.exit("Invalid usage")
