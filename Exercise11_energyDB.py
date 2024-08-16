""" Build a database of energy sources in the US. """


from argparse import ArgumentParser
import sqlite3
import sys


class EnergyDB:
    """Represents and works with an energy production database.
    
    Attributes:
        filename(str): a given file path.
    
    """

    def __init__(self, filename):
        """Initializes variables for the EnergyDB class and creates an in memory sqlite database.
        
        Args:
            filename(str): a given file path
        
        """

        self.conn = sqlite3.connect(':memory:')
        self.read(filename)
    
    def __del__(self):
        """ Clean up the database connection. """
        try:
            self.conn.close()
        except:
            pass
    
    def read(self, filename):
        """Inserts data into the 'production' table and reads a file.
        
        Args:
            filename: a given file path.
        
        """
        cursor = self.conn.cursor()
        cursor.execute( '''CREATE TABLE production
        (year integer, state text, source text, mwh real)''')

        with open(filename, 'r') as file:
            next(file)                          #skips first line
            for line in file:
                data = line.strip().split(',')
                year = int(data[0])
                state = data[1]
                source = data[2]
                mwh = float(data[3])

                cursor.execute ('''INSERT INTO production VALUES (?,?,?,?)''', (year, state, source, mwh))

            self.conn.commit
        
    def production_by_source(self, source, year):
        """Sums up and calculates the total megawatt hours from a specific source and year
        
        Args:
            source(str): a given energy source
            year(int): a specific year to search by.
            
        Returns:
            float: the total megawatt hours from a given source and year.
        
        """

        cursor = self.conn.cursor()
        cursor.execute('''SELECT mwh FROM production WHERE source=? AND year=?''', (source, year))
        
        db_rows = cursor.fetchall()

        sum_mwh = sum(row[0] for row in db_rows)
        return sum_mwh
            


def main(filename):
    """ Build a database of energy sources and calculate the total production
    of solar and wind energy.
    
    Args:
        filename (str): path to a CSV file containing four columns:
            Year, State, Energy Source, Megawatthours.
    
    Side effects:
        Writes to stdout.
    """
    e = EnergyDB(filename)
    sources = [("solar", "Solar Thermal and Photovoltaic"),
               ("wind", "Wind")]
    for source_lbl, source_str in sources:
       print(f"Total {source_lbl} production in 2017: ",
             e.production_by_source(source_str, 2017))


def parse_args(arglist):
    """ Parse command-line arguments. """
    parser = ArgumentParser()
    parser.add_argument("file", help="path to energy CSV file")
    return parser.parse_args(arglist)


if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args.file)