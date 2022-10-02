"""Demonstrates details of writing Python functions: annotations, default args, kwargs.
"""


# def demonstrate_annotations(title, year):
def demonstrate_annotations(title: str, year: int) -> str:
    """Demonstrates how to use annotations of
    function parameters/arguments (<arg>: <type>) and of function return type (def f(...) -> <type>:).
    - print the function parameters/arguments
    - print the value of the __annotations__ attribute of this function
    - print the name and the docstring of this function
    - return a formatted string (including function parameters/arguments)
    """

    print(title + ',', year)
    print(demonstrate_annotations.__annotations__)
    print(demonstrate_annotations.__name__ + ':\n', demonstrate_annotations.__doc__)
    return f'Calling {demonstrate_annotations.__name__}("{title}", {year}).'


# def show_song(title, author='Paul McCartney', year: int = 1969):
def show_song(title, author='Paul McCartney', year=1969):

    """Demonstrates default arguments/parameters.
    - print locals()
    - print the function arguments/parameters in one line
    """

    print(locals())
    print(f'{title}, {author}, {year}')


def use_flexible_arg_list(band: str, *members):
    """Demonstrates flexible number of arguments/parameters.
    - print the band name and the list of band members in one line
    """

    print(members)
    print(*members)
    # # print(type(members))        # <class 'tuple'>
    # # print(type(*members))       # TypeError
    # print()
    # s = f'{band}: {members}' if members else f'{band}'
    # print(s)
    # print()
    print(f'{band}: ' + ', '.join([members[i] for i in range(len(members))]))


def use_all_categories_of_args(band, *members, is_active=True, **details):
    """Demonstrates positional args, flexible args, keyword args, and kwargs (flexible keyword args).
    - print all arguments/parameters, including the keyword arguments/parameters, in one line
    """

    b = f'{band}:' if band else 'Unknown band:'
    m = ', '.join([members[i] for i in range(len(members))]) if len(members) else 'members unknown'
    m += ';'
    a = 'active' if is_active else 'not active'
    a += ';'
    d = ', '.join([str(k) + ': ' + str(v) for k, v in details.items()])
    print(b, m, a, d)


if __name__ == "__main__":

    song = 'Oh! Darling'
    year = 1969

    john = 'John Lennon'
    paul = 'Paul McCartney'
    george = 'George Harrison'
    ringo = 'Ringo Starr'
    the_beatles = [john, paul, george, ringo]

    # print(demonstrate_annotations(song, year))

    # show_song(song)

    use_flexible_arg_list('The Beatles', *the_beatles)
    # use_flexible_arg_list('The Beatles')

    use_all_categories_of_args('The Beatles', is_active=False, start=1962, end=1970)
    use_all_categories_of_args('The Beatles', *the_beatles, is_active=False, start=1962, end=1970)

