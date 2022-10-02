"""The class representing the concept of a music group/band.
It includes a list of Musician objects (band members) and the date when the band started performing together.
"""

from datetime import date, datetime, time
import json

# from music.musician import Musician
# from util.utility import format_date


class Band():
    """The class describing the concept of a music group/band.
    It includes a list of Musician objects (band members)
    and the dates when the band started/stopped performing together.
    """

    # Class variables: like static fields in Java; typically defined and initialized before __init__()
    # Insert a class variable (static field), such as genres, date_pattern,...

    def __init__(self, name, *members, start=date.today(), end=date.today()):
        pass                                            # introduce and initialize iterator counter, self.__i

    def __str__(self):
        pass

    def __eq__(self, other):
        # Musician objects are unhashable, so comparing the members tuples from self and other directly does not work;
        # see https://stackoverflow.com/a/14721133/1899061, https://stackoverflow.com/a/17236824/1899061
        # return self == other if isinstance(other, Band) else False    # No! Musician objects are unhashable!

        pass

    def parse_band_str(self, band_str):
        """Splits a band string in its typical segments.
        """
        pass

    @staticmethod
    def is_date_valid(d):
        """It is assumed that a band does not perform together since more than ~60 years ago.
        So, the valid date to denote the start of a band's career is between Jan 01, 1960, and today.
        """

        pass

    def __iter__(self):
        """Once __iter__() and __next__() are implemented in a class,
        we can create an iterator object by calling the iter() built-in function on an object of the class,
        and then call the next() built-in function on that object.
        It is often sufficient to just return self in __iter__(),
        if the iterator counter such as self.__i is introduced and initialized in __init__().
        Alternatively, the iterator counter (self.__i) is introduced and initialized here.
        """

        pass
        # return self               # sufficient if the iterator counter is introduced and initialized in __init__()

    def __next__(self):
        pass


def next_member(band):
    """Generator that shows members of a band, one at a time.
    yield produces a generator object, on which we call the next() built-in function.
    A great tutorial on generators: https://realpython.com/introduction-to-python-generators/.
    """

    pass


class BandEncoder(json.JSONEncoder):
    """JSON encoder for Band objects (cls= parameter in json.dumps()).
    """

    def default(self, band):
        # recommendation: always use double quotes with JSON

        pass


def band_py_to_json(band):
    """JSON encoder for Band objects (default= parameter in json.dumps()).
    """


def band_json_to_py(band_json):
    """JSON decoder for Band objects (object_hook= parameter in json.loads()).
    """


if __name__ == "__main__":

    # from testdata.musicians import *

    # Check class variables (like static fields in Java; typically defined and initialized before __init__())
    print()

    # Check the basic methods (__init__(), __str__(),...)
    print()

    # Check the alternative constructor 1 (@classmethod from_band_str_year(<band_str>))
    print()

    # Check the alternative constructor 2 (@classmethod from_band_str_date(<band_str>))
    print()

    # Check date validator (@staticmethod is_date_valid(<date>))
    print()

    # Check the iterator
    print()

    # Repeated attempt to run the iterator fails, because the iterator is exhausted

    # Demonstrate generators
    print()

    # Demonstrate generator expressions
    print()

    # Demonstrate JSON encoding/decoding of Band objects
    # Single object
    print()

    # List of objects
    print()


