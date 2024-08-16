from argparse import ArgumentParser
import pandas
import sys


def most_educated(csv_path, state_abv):

    data_frame = pandas.read_csv(csv_path)
    new_frame = data_frame["State"] == state_abv
    state_fiter = data_frame[new_frame]
    per_adults = state_fiter["Percent of adults with a bachelor's degree or higher"].max()
    highest_county = state_fiter[state_fiter["Percent of adults with a bachelor's degree or higher"] == per_adults]
    county_name = highest_county["Area name"].iloc[0]

    return (county_name, per_adults)

def parse_args(arglist):
    parser = ArgumentParser(description= "Gets percentage of adults who have at least a bachelors degree in a given state")
    parser.add_argument("csv_path", type= str, help= "a path to a CSV file")
    parser.add_argument("state_abv", type= str, help= "a two-letter state abbreviation, such as MD")

    return parser.parse_args(arglist)

if __name__ == "__main__":
    parse = parse_args(sys.argv[1:])
    county_name, per_adults = most_educated(parse.csv_path, parse.state_abv)
    print(f"{per_adults} of adults in {county_name} have at least a bachelors degree.")















