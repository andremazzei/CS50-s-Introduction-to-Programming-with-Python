'''
One of David’s first toys as a child, funny enough, was Little Professor, a “calculator” that would
generate ten different math problems for David to solve. For instance, if the toy were to display 4 + 0 = ,
David would (hopefully) answer with 4. If the toy were to display 4 + 1 = , David would (hopefully) answer
with 5. If David were to answer incorrectly, the toy would display EEE. And after three incorrect answers
for the same problem, the toy would simply display the correct answer (e.g., 4 + 0 = 4 or 4 + 1 = 5).

In a file called professor.py, implement a program that:

Prompts the user for a level,
. If the user does not input 1, 2, or 3, the program should prompt again.
Randomly generates ten (10) math problems formatted as X + Y = , wherein each of X and Y is a non-negative
integer with
 digits. No need to support operations other than addition (+).
Prompts the user to solve each of those problems. If an answer is not correct (or not even a number),
the program should output EEE and prompt the user again, allowing the user up to three tries in total
for that problem. If the user has still not answered correctly after three tries, the program should o
utput the correct answer.
The program should ultimately output the user’s score: the number of correct answers out of 10.
Structure your program as follows, wherein get_level prompts (and, if need be, re-prompts) the user for
a level and returns 1, 2, or 3, and generate_integer returns a randomly generated non-negative integer
with level digits or raises a ValueError if level is not 1, 2, or 3:
'''

import random


def main():
    level = get_level()
    tries = 0
    correct_count = 0
    wrong_count = 0
    while tries < 10:
        first_num = generate_integer(level)
        second_num = generate_integer(level)
        while True:
            print(first_num, "+", second_num, "= ", end="")
            try:
                result = int(input(""))
                if first_num + second_num == result:
                    correct_count += 1
                    tries += 1
                    break
                elif first_num + second_num != result:
                    wrong_count += 1
                    print("EEE")
                    if wrong_count == 3:
                        print(first_num, "+", second_num, "=", first_num + second_num)
                        tries += 1
                        wrong_count = 0
                        break
            except ValueError:
                if wrong_count < 2:
                    wrong_count += 1
                    print("EEE")

                elif wrong_count == 2:
                    print("EEE")
                    print(first_num, "+", second_num, "=", first_num + second_num)
                    tries += 1
                    break

    print("Score:", correct_count)


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level > 0 and level < 4:
                return level
        except:
            pass


def generate_integer(level):
    if level == 1:
        number = random.randrange(0, 10)
        return number
    elif level == 2:
        number = random.randrange(10, 100)
        return number
    else:
        number = random.randrange(100, 1000)
        return number


if __name__ == "__main__":
    main()
