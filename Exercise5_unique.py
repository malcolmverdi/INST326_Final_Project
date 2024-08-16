import re


def get_words(s):
    """ Extract a list of words from string s.

    Args:
        s (str): a string containing one or more words.

    Returns:
        list of str: a list of words from s converted to lower-case.
    """
    words = list()
    s = re.sub(r"--+", " ", s)
    for word in re.findall(r"[\w'-]+", s):
        word = word.strip("'-_")
        if len(word) > 0:
            words.append(word.lower())
    return words

class UniqueWords:
    """Obtain unique words specified by a given file.
    
    Attributes:
        all_words(set): keeps track of every word you encounter in the files you read in.
        unique_words(set): keeps track of words that only appear in a single file.
        words_by_file(dict): keeps track of the words that occur in a single file.
        
    """
    def __init__(self):
        """Initialize a new object for UniqueWords class.

        Side effects:
            Sets attributes all_words, unique_words, and words_by_file.
        """
        self.all_words = set()
        self.unique_words = set() 
        self.words_by_file = {} 
   
    def add_file(self, filename, key):
        """Opens and reads a file to then add words to UniqueWords
        
        Args:
            filename (str): essentially the file path. Helps to locate the file.
            key (str): gives a way to identify words in the words_by_file dictionary.
            
        Side effects:
            Updates the attributes initialized in the __init__ function (all_words, unique_words, and words_by_file).
        """
        with open(filename, "r") as key:
            file_read = key.read()
            set_words = set(get_words(file_read))
            self.words_by_file[key] = set_words
            self.unique_words -= set_words
            new_words = set_words - self.all_words

            self.unique_words.update(new_words)
            self.all_words.update(set_words)

    def unique(self, key):
        """Produces a set of unique words from a given file.
        
        Args:
            key(str): gives a way to identify words in the words_by_file dictionary.
        
        Returns:
            set: a set of unique words from a given file."""
        return self.words_by_file.get(key, set())
    





