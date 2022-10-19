"""Demonstrates working with lists.
"""


#%%
def demonstrate_lists():
    """Using just the simplest operations with lists.
    - create a non-empty list with different kinds of elements
    - accessing/slicing a list
    - comparing 2 lists (== vs. is)
    - concatenating 2 lists (the + operator)
    - looping through a list
    """

    paul = ['Paul McCartney', 1942, True]

    print(paul[0])
    print(paul[1:])
    print(paul[:-1])
    print(paul == ['Paul McCartney', 1942, True])
    print(paul is ['Paul McCartney', 1942, True])
    print(paul + ['Liverpool'])
    for i in paul:
        print(i)
    print()


#%%
# Test demonstrate_lists()
demonstrate_lists()


#%%
def demonstrate_list_methods():
    """Using
    append()
    insert()
    remove()
    pop()
    extend()
    count()
    index()
    reverse()
    len()
    ...
    Also, "in" and "not in" operators can be used to search lists
    for the occurrence of a given element.
    """

    paul = ['Paul McCartney', 1942, True]
    print(paul)
    print()

    print(paul.append('Liverpool'))
    print(paul)
    print(paul.insert(2, 'The Beatles'))
    print(paul)
    paul.remove('The Beatles')
    print(paul)
    paul.pop(1)
    print(paul)
    paul.extend(['The Beatles'])
    print(paul)
    print(paul.count(True))
    print(paul.index('The Beatles'))
    paul.reverse()
    print(paul)
    print(len(paul))
    print()


#%%
# Test demonstrate_list_methods()
demonstrate_list_methods()


#%%
def demonstrate_arrays():
    """Using array.array() to build list-based numeric arrays.
    Demonstrating that lists and arrays are different types.
    """

    from array import array
    a = array('i', [1, 2, 3, 4])
    print(a)
    print(type(a))
    print()


#%%
# Test demonstrate_arrays()
demonstrate_arrays()


#%%
def populate_empty_list():
    """Creating an empty list and populating it with random values
    using random.seed() and random.randint()
    """

    from random import randint, seed
    l = []
    seed(12)
    for i in range(100):
        l.append(randint(0, 1000))
    print(l[23:34])
    print()


#%%
# Test populate_empty_list()


#%%
def duplicate_list():
    """Duplicating lists (carefully :)).
    Don't use l2 = l1, but either of the following:
    - l2 = l1.copy()
    - l2 = l1 + []
    - l2 = l1[:]
    """

    paul = ['Paul McCartney', 1942, True]
    mcCartney = paul
    print(mcCartney is paul)
    mcCartney = paul.copy()
    print(mcCartney is paul)
    print()


#%%
# Test duplicate_list()
duplicate_list()


#%%
def demonstrate_list_comprehension():
    """Showing examples of list comprehension.
    - list comprehension over a list of strings
    - list comprehension with enumerate(), to find indices of all occurrences of an element in a list
    Using str() and join() in printing results.
    """

    songs = ['Hey Jude', 'Eleanor Rigby', 'Let It Be', 'Penny Lane']

    print([song for song in songs if 'L' in song])

    fw = [title.split()[0] for title in songs]
    print(fw)
    fl = [w[0] for w in fw]
    print(fl)
    result = ''.join([l for l in fl]).capitalize() + '!'
    print(result)


#%%
# Test demonstrate_list_comprehension()
demonstrate_list_comprehension()
