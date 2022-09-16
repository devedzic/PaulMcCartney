"""The very first module in a more structured version of the project.
"""


# Moving code from main.py

def year_of_birth():
    """A simple function defined in a module
    """

    print('Paul McCartney was born in: ', end='')
    year = input()
    return year


# Taking care of the module __name__

if __name__ == '__main__':

    # Hello world: the print() built-in function and the + operator.

    # print('Paul McCartney')
    # print('Paul McCartney', 'was born in', 1942)
    # # print('Paul McCartney', 'was born in', 1942 + '.')
    # print('Paul McCartney', 'was born in', str(1942) + '.')
    # print('Paul McCartney wrote \'Yesterday\' in \n' + str(1965))
    #
    # # The input() built-in function
    #
    # # print('Paul McCartney was born in: ')
    # # year = input()
    # # print('Paul McCartney was born in: ', end='')
    # # year = input()
    # # print('Paul McCartney was born in:', year + '.')
    #
    # print('Paul McCartney was born in:', int(input()))
    #
    # # A simple function and function call
    #
    # print(year_of_birth())

    # A simple loop and the range() built-in function

    # for i in range(5):
    #     print(i)
    # print()

    # i = 0
    # while i < 5:
    #     print(i)
    #     i += 1
    #
    # # A simple list, accessing list elements, printing lists
    #
    # songs = ['Oh, Darling', 'The Long and Winding Road', 'She\'s a Woman']
    # print(songs[2])
    # print(songs)
    # print('; '.join(songs) + '.')
    #
    # # Looping through list elements - for and enumerate()
    #
    # for i in range(len(songs)):
    #     print(songs[i])
    # print()
    #
    # for i, song in enumerate(songs):
    #     print(str(i + 1) + ':', song)
    # print()
    #
    # print(enumerate(songs))
    # print(list(enumerate(songs)))
    # print(list(enumerate(songs, start=1)))
    # print()
    #
    # for i, song in enumerate(songs, start=1):
    #     print(str(i) + ':', song)
    #
    # # Global variables: __name__, __file__, __doc__,...
    #
    # print(__name__)
    # # print(__file__)   # Doesn't work from a notebook and from a .py generated from a notebook, just from an original .py
    # print(__doc__)
    # print(globals())

    # Printing with ' ' and printing without '\n'


    # Printing with classical formatting (%)

    # city = 'Liverpool'
    # year = 1942
    # print('Paul McCartney was born in %s, in %d ' % (city, year))

    # Printing with f-strings

    # city = 'Liverpool'
    # year = 1942
    # print(f'Paul McCartney was born in {city}, in {year}.')

    # Keyboard input

    # break and continue

    # for i in range(5):
    #     if i == 2:
    #         break
    #         # continue
    #     print(i)
    # print()

    # Printing docstrings

    # print(year_of_birth.__doc__)

    # Printing a list using enumerate()

    # songs = ['The Long and Winding Road', 'Let It Be', 'Rocky Racoon']
    # for i, song in enumerate(songs, start=1):
    #     print(i, song)

    # Importing from Standard Library

    # Date format strings
    # https://docs.python.org/3/library/datetime.html?highlight=date%20format%20strings#strftime-and-strptime-format-codes

    from datetime import date
    d = date(1942, 6, 18)
    print(d)
    date_formatting_string = '%b %d, %Y'
    print(d.strftime(date_formatting_string))

    # Testing print(__file__)
    print(__file__)
