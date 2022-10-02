"""The class representing the concept of a music group/band.
It includes a list of Musician objects (band members) and the date when the band started performing together.
"""

from datetime import date, datetime, time
import json

from music.musician import Musician
from util.utility import format_date


class Band():
    """The class describing the concept of a music group/band.
    It includes a list of Musician objects (band members)
    and the dates when the band started/stopped performing together.
    """

    # Class variables: like static fields in Java; typically defined and initialized before __init__()
    # Insert a class variable (static field), such as genres, date_pattern,...

    genres = ['rock', 'blues', 'pop', 'alternative', 'unknown']

    def __init__(self, name, *members, start=date.today(), end=date.today()):
        # pass                                            # introduce and initialize iterator counter, self.__i
        self.name = name
        self.members = members
        self.start = start
        self.end = end
        self.__i = 0

    def __str__(self):
        n = self.name
        m = f'({", ".join([member.name for member in self.members]) if self.members else "members unknown"})'
        s = self.start.year
        e = self.end.year
        return f'{n} {m}, {s}-{e}'

    def __eq__(self, other):
        # Musician objects are unhashable, so comparing the members tuples from self and other directly does not work;
        # see https://stackoverflow.com/a/14721133/1899061, https://stackoverflow.com/a/17236824/1899061
        # return self == other if isinstance(other, Band) else False    # No! Musician objects are unhashable!

        t = isinstance(other, Band)
        n = self.name == other.name

        # # members must be compared 'both ways', because the two tuples can be of different length
        # m_diff_1 = [x for x in self.members if x not in other.members]
        # m_diff_2 = [x for x in other.members if x not in self.members]
        # m = len(m_diff_1) == len(m_diff_2) == 0

        # members must be compared 'both ways', because the two tuples can be of different length
        m = all([x in self.members for x in other.members]) and all([x in other.members for x in self.members])

        y = (self.start == other.start) and (self.end == other.end)
        return t and n and m and y

    @staticmethod
    def is_date_valid(d):
        """It is assumed that a band does not perform together since more than ~60 years ago.
        So, the valid date to denote the start of a band's career is between Jan 01, 1960, and today.
        """

        return date(1954, 7, 5) <= d <= date.today() if isinstance(d, date) else False

    def __iter__(self):
        """Once __iter__() and __next__() are implemented in a class,
        we can create an iterator object by calling the iter() built-in function on an object of the class,
        and then call the next() built-in function on that object.
        It is often sufficient to just return self in __iter__(),
        if the iterator counter such as self.__i is introduced and initialized in __init__().
        Alternatively, the iterator counter (self.__i) is introduced and initialized here.
        """

        self.__i = 0
        return self               # sufficient if the iterator counter is introduced and initialized in __init__()

    def __next__(self):
        if self.__i < len(self.members):
            next_m = self.members[self.__i]
            self.__i += 1
            return next_m
        else:
            raise StopIteration


def next_member(band):
    """Generator that shows members of a band, one at a time.
    yield produces a generator object, on which we call the next() built-in function.
    A great tutorial on generators: https://realpython.com/introduction-to-python-generators/.
    """

    for member in band.members:
        input('Next: ')
        yield member
        print('Yeah!')


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

    from testdata.musicians import *

    # Check class variables (like static fields in Java; typically defined and initialized before __init__())
    print(Band.genres)
    print()

    # Check the basic methods (__init__(), __str__(),...)
    theBeatles = Band('The Beatles', *[johnLennon, paulMcCartney, georgeHarrison, ringoStarr, ],
                      start=date(1957, 7, 6), end=date(1970, 4, 10))
    print(theBeatles)
    beatles = Band('The Beatles', *[johnLennon, georgeHarrison, paulMcCartney, ringoStarr, Musician('Pete Best')],
                   start=date(1957, 7, 6), end=date(1970, 4, 10))
    print(theBeatles == beatles)
    # print(set(list(theBeatles.members)) == set([johnLennon, georgeHarrison, paulMcCartney, ringoStarr]))
    # print(type(theBeatles.members))
    # print(set(theBeatles.members))
    print()

    # Check date validator (@staticmethod is_date_valid(<date>))
    print(Band.is_date_valid(date(1957, 7, 6)))
    print()

    # Check the iterator
    for _ in range(len(theBeatles.members)):
        print(theBeatles.__next__().name)
    # print(theBeatles.__next__().name)             # iterator exhausted, must be re-initiated
    print()

    # i = iter(theBeatles)
    # print(i)
    i = iter(theBeatles)                            # re-initiating the iterator
    for _ in range(len(theBeatles.members)):
        print(next(theBeatles))
    print()

    # # Alternatively
    # theBeatles.__iter__()
    # for _ in range(len(theBeatles.members)):
    #     print(theBeatles.__next__().name)
    # print()

    # Repeated attempt to run the iterator fails, because the iterator is exhausted

    # # Demonstrate generators
    # member_generator = next_member(theBeatles)
    # print(member_generator)
    # print(type(member_generator))
    # print()
    #
    # while True:
    #     try:
    #         print(next(member_generator))
    #     except:
    #         break
    # print()

    # Demonstrate generator expressions
    print(i**2 for i in range(4))
    print(next((i**2 for i in range(4))))
    print(next((i**2 for i in range(4))))
    ge = (i**2 for i in range(4))
    print(ge)
    print(next(ge))     # 0
    print(next(ge))     # 1
    print(next(ge))     # 4
    print(next(ge))     # 9
    print(next(ge))     # raises StopIteration
    print()

    # Demonstrate JSON encoding/decoding of Band objects
    # Single object
    print()

    # List of objects
    print()


