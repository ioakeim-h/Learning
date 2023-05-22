import sys
import requests
import json


def main():
    n = buy()
    usd = exchange(n)
    print(f"${usd:,.4f}")


def buy():
    if len(sys.argv) == 2:
        try:
            return float(sys.argv[1])
        except ValueError:
            sys.exit("Command-line argument is not a number")
    else:
        sys.exit("Missing command-line argument")


def exchange(bitcoin):
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        data = response.json()
        return data["bpi"]["USD"]["rate_float"] * bitcoin
    except requests.RequestException:
        sys.exit("An error occurred")


main()

