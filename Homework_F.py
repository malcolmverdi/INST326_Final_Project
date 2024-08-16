""" Sort books by Library of Congress call number. """


from argparse import ArgumentParser
import re
import sys


class Book:
    """Organizes books by their call number.
        
    Attributes:
        callnum(str): the call number for the book.
        title(str): the title of the book.
        author(str): the author of the book.
    
    """
    def __init__(self, callnum, title, author = None):

        self.callnum = str(callnum)
        self.title = str(title)
        self.author = str(author) if author is not None else None

    def __lt__(self, other):
        """Takes data from the callnum_parts function and verifys they're sorted correctly.
        
        Args:
            other: an instance of the Book class
        
        Returns:
            bool: a value based on whether or not the parts of the call number are sorted correctly.
        
        """
        self_callnum = self.callnum_parts(self.callnum)
        other_callnum = other.callnum_parts(other.callnum)
        if self_callnum < other_callnum:
            return True
        else:
            return False
    
    def callnum_parts(self, callnum):
        """Matches parts of a call number to elements of a regular expression.
        
        Args:
            callnum(str): the call number for the book
        
        Returns:
            tuple: a tuple that holds each element of a call number.

        """
        callnum_exp = r'([A-Z]+)\s*(\d+(\.\d+)?)\s*(\.\w+\d*)?\s*([A-Z]+\d*)?\s*(\d{4})?$'

        match = re.match(callnum_exp, callnum)

        letters = match.group(1) if match.group(1) else ''
        nums = float(match.group(2)) if match.group(2) else ''
        cutter = match.group(4) if match.group(4) else ''
        double_cutter = match.group(5) if match.group(5) else ''
        year = match.group(6) if match.group(6) else ''

        return (letters, nums, cutter, double_cutter, year)


    def __repr__(self):
        """Takes an instance of book and converts it into a string.
        
        Returns:
            str: a string containing a book's call number, title, and author.
        
        """
        book = (f'Book {repr(self.callnum)}, {repr(self.title)}, {repr(self.author)}')

        return book
    

def read_books(filename):
    """Reads a file and adds data about books in the file to a list.
    
    Args:
        filename(str): a file path
    
    Returns:
        list: a list containing each element of a book.
    
    """
    book_list = []

    with open(filename, 'r', encoding= 'utf-8') as file:
        for line in file:
            book_var = line.strip().split('\t')
            title, author, callnum = book_var
            book = Book(callnum, title, author)
            book_list.append(book)

    return book_list


def print_books(books):
    """ Print information about each book, in order. """
    for book in sorted(books):
        print(book)


def main(filename):
    """ Read book information from a file, sort the books by call number,
    and print information about each book. """
    books = read_books(filename)
    print_books(books)


def parse_args(arglist):
    """ Parse command-line arguments. """
    parser = ArgumentParser(arglist)
    parser.add_argument("filename", help="file containing book information")
    return parser.parse_args(arglist)


if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args.filename)
