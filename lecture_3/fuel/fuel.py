"""
Fuel gauges indicate, often with fractions, just how much fuel is in a tank.
For instance 1/4 indicates that a tank is 25% full, 1/2 indicates that a tank
is 50% full, and 3/4 indicates that a tank is 75% full.

In a file called fuel.py, implement a program that prompts the user for a fraction,
formatted as X/Y, wherein each of X and Y is an integer, and then outputs, as a
percentage rounded to the nearest integer, how much fuel is in the tank. If, though,
1% or less remains, output E instead to indicate that the tank is essentially empty.
And if 99% or more remains, output F instead to indicate that the tank is essentially full.

If, though, X or Y is not an integer, X is greater than Y, or Y is 0, instead prompt
the user again. (It is not necessary for Y to be 4.) Be sure to catch any exceptions
like ValueError or ZeroDivisionError.
"""


def main():
    fraction = converter("Fraction: ")
    print(results(fraction))

# convert fraction to percentage
def converter(data):
    while True:
        try:
            c = input(data)
            x, y = c.split("/")
            x= int(x)
            y = int(y)
            if x < y or x == y:
                result = x / y *100
                return result
        except (ValueError, ZeroDivisionError):
            pass

# output final result
def results(r):
    if r >= 99 :
        return "F"
    if r <= 1 :
        return "E"
    else:
        return f"{round(r)}%"

main()
