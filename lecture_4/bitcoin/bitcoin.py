'''
Bitcoin is a form of digital currency, otherwise known as cryptocurrency. Rather than rely on a central authority
like a bank, Bitcoin instead relies on a distributed network, otherwise known as a blockchain, to record transactions.

Because there’s demand for Bitcoin (i.e., users want it), users are willing to buy it, as by exchanging one currency
(e.g., USD) for Bitcoin.

In a file called bitcoin.py, implement a program that:

Expects the user to specify as a command-line argument the number of Bitcoins,
, that they would like to buy. If that argument cannot be converted to a float, the program should exit via sys.exit
with an error message.
Queries the API for the CoinDesk Bitcoin Price Index at https://api.coindesk.com/v1/bpi/currentprice.json, which
returns a JSON object, among whose nested keys is the current price of Bitcoin as a float. Be sure to catch any
exceptions, as with code like:
import requests

try:
    ...
except requests.RequestException:
    ...
Outputs the current cost of
 Bitcoins in USD to four decimal places, using , as a thousands separator.
'''

import sys
import requests

def main():
    x = get_cla()
    y = query_bitcoin()
    print(f"${x*y:,.4f}")

# command-line argument the number of Bitcoins. needs to be a float, otherwise exit.
def get_cla():
    if len(sys.argv) == 1:
        sys.exit("Missing command-line argument")
    elif len(sys.argv) > 2:
        sys.exit
    else:
        try:
            quantity = float(sys.argv[1])
            return quantity

        except:
            sys.exit("Command-line argument is not a number")

# Query bitcoin
def query_bitcoin():
    try:
        r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        o = r.json()
        price = o["bpi"]["USD"]["rate_float"]
        return price
    except requests.RequestException:
        print("Request Exception")

# output $ with 4 decimals using comma.
#print(f"${amount:,.4f}")

if __name__ == "__main__":
    main()
