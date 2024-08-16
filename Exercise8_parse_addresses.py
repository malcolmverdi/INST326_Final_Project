from argparse import ArgumentParser
import re
import sys

def parse_address(text):
    """Scans text and searches for parts of an address.
    
    Args:
        text(str): a single line of text that is examined for containing address attributes.
    
    Returns:
        dict: a dictionary containing keys that make up an address.
    
    """

    address_match = re.search(r'^(?P<house_number>\d+)\s+(?P<street>[\w\s]+),\s+(?P<city>[\w\s]+)\s+(?P<state>[A-Z]{2})\s+(?P<zip>\d{5})$', text)
    address_dict = {}
    if address_match:
        address_dict["house_number"] = address_match.group(1)
        address_dict["street"] = address_match.group(2)
        address_dict["city"] = address_match.group(3)
        address_dict["state"] = address_match.group(4)
        address_dict["zip"] = address_match.group(5)
        return address_dict
    else:
        return None



def parse_addresses(filename):
    """Opens a file and adds the address dictionaries to a list.
    
    Args:
        filename(str): the path of the file.
    
    Returns:
        list: a list of dictionaries which holds the addresses.
    
    """

    with open (filename, 'r') as address:
        newlist = [parse_address(line) for line in address]
        
    return newlist


def parse_args(arglist):
    """ Parse command-line arguments. """
    parser = ArgumentParser()
    parser.add_argument("file",
                        help="file containing one address per line")
    return parser.parse_args(arglist)

if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    for address in parse_addresses(args.file):
        print(address)
