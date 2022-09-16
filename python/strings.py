"""Demonstrates working with strings in Python.
"""

import string

import settings


def demonstrate_formatting():
    """Demonstrating details of string formatting.
    - using classical formatting
    - \n is the new line char
    - r'...' - raw formatting
    - using \"\"\"...\"\"\" for multi-line formatting
    - string "multiplication"
    - substrings / slicing
    - str() vs. repr() (usually the same, but with whitespace there is a difference)
    """

    print('Sir %s is %d now.' % ('Paul', 80))
    print()

    print('C:\notebooks')
    print()

    print(r'C:\notebooks')
    print()

    print("""Paul
    McCartney""")
    print()

    print('Paul McCartney\t' * 3)
    print()

    print('Paul McCartney')
    print('Paul McCartney'[5:])
    print('Paul McCartney'[5:8])
    print('Paul McCartney'[:8])
    print('Paul McCartney'[5:-3])
    print('Paul McCartney'[5:])
    print('Paul McCartney'[-7:-3])
    print()

    print(str('Paul McCartney'))
    print(repr('Paul McCartney'))
    print(str('Paul McCartney\t'))
    print(repr('Paul McCartney\t'))
    print()

def demonstrate_fancy_formatting():
    """Using "fancy" formatting.
    - format strings like '{0}{1} {2}', '{0}{1} {2}, {3}', etc.
    """

    print('Sir {0} was born in {1} in {2}.'.format('Paul McCartney', 'Liverpool', 1942))
    print()


def demonstrate_fancy_formatting_with_f_strings():
    """Using f-strings in formatting.
    - format strings like f'Some text {some var}, more text {another var}...', etc.
    """

    name = 'Paul McCartney'
    city = 'Liverpool'
    year = 1942
    print(f'Sir {name} was born in {city} in {year}.')
    print()


def demonstrate_string_operations():
    """Using different string operations.
    - endswith(), split(), center(), in (aka contains()), == (aka equals()), len(), ..., strip() (lstrip(), rstrip())
    """

    from datetime import date
    from util.utility import format_date
    d = date(1957, 7, 6)

    bigBang = f'Paul McCartney met John Lennon for the first time on {format_date(d)} in Woolton.'

    print(bigBang.endswith('Woolton'))
    print(bigBang.split())
    print(bigBang.split('in '))
    print(' Paul McCartney '.center(30, '*'))
    print('John Lennon' in bigBang)
    print(bigBang.split()[0] == 'Paul')
    print(len(bigBang))
    print('         Paul McCartney            '.strip())
    print('         Paul McCartney            '.rstrip())
    print()


if __name__ == '__main__':

    demonstrate_formatting()
    demonstrate_fancy_formatting()
    demonstrate_fancy_formatting_with_f_strings()
    demonstrate_string_operations()
