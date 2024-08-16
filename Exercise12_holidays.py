from argparse import ArgumentParser
import requests
import sys


def get_holidays(country_code, year):
    url = f"https://date.nager.at/api/v3/publicholidays/{year}/{country_code}"

    request = requests.get(url)
    results = request.json()

    for result in results:
        print(f"{result['date']}: {result['localName']}")

def parse_args(arglist):
    parser = ArgumentParser()
    parser.add_argument("country_code", type= str, help= "A two letter abbreviation for a country.")
    parser.add_argument("year", type= int, help= "Represents the date of the holiday.")
    return parser.parse_args(arglist)

if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    get_holidays(args.country_code, args.year)