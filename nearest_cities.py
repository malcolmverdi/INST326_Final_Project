""" Find cities near a specified location. """
from argparse import ArgumentParser
import sys

from haversine import haversine

class Cities:
    """Retrives information about cities and finds the nearest cities to a specified 
    latitude and longitude.
    
    Attributes:
        cities (dict): a dictionary containing data about cities derived from a given file
    
    """
    
    def __init__(self, filename):
        """Initializes a dictionary for the 'Cities' class and orgaizes the stored data in a set order
        with corrected data types. 
        
        Args:
            filename (str): the path of a given file containing city data.

        """
        self.cities = {}
        with open (filename, 'r') as key:
            for line in key:
                key_attributes = line.split(",")
                area = key_attributes[0]
                city = key_attributes[1]
                latitude = key_attributes[2]
                longtitude = key_attributes[3]
                self.cities[(area, city)] = float(latitude), float(longtitude)
    
    def nearest(self, point):
        """Sorts the keys of the cities attribute according to their distance from point.
        
        Args:
            point(float): a tuple consisting of the longtitude and latitude expressed as floats.
            
        Returns:
            sort_cities: returns the five closest cities to a given point.

        """
        sort_cities = sorted(
            self.cities.keys(),
            key = lambda c: (haversine(point, self.cities[c]))
        )
        return sort_cities[:5]
    
def main(filename, arg1, arg2):
    """ Read city data from a file and find the closest cities to a
    specified location (either an area and city from filename or a
    latitude and longitude which may or may not be in the file).

    Args:
        filename (str): path to a file containing city data. Each line
            in the file should consist of four values, separated by
            commas: area (e.g., state or country), city, latitude in
            decimal degrees, longitude in decimal degrees.
        arg1 (str): either the name of an area in the file, or a string
            representation of a latitude.
        arg2 (str): either the name of a city in the file, or a string
            representation of a longitude.
    Side effects:
        Writes to stdout.
    """
    cities = Cities(filename)
    try:
        lat = float(arg1)
        lon = float(arg2)
        point = (lat, lon)
    except ValueError:
        try:
            point = cities.cities[arg1, arg2]
        except KeyError:
            sys.exit(f"Error: could not look up {arg1}, {arg2}")
    print(f"For {arg1}, {arg2}, the nearest cities from the file are")
    for result in cities.nearest(point):
        print(" " + ", ".join(result))

def parse_args(arglist):
    """ Process command-line arguments and return the parsed values as a
    namespace. """
    parser = ArgumentParser()
    parser.add_argument("filename", help="file containing city data")
    parser.add_argument("arg1", 
                        help="a latitude expressed in decimal degrees"
                             " or an area (state, country) from the"
                             " file")
    parser.add_argument("arg2",
                        help="a longitude expressed in decimal degrees"
                             " or a city name from the file")
    return parser.parse_args(arglist)
if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args.filename, args.arg1, args.arg2)