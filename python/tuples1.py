"""Demonstrates tuples.
"""


#%%
def demonstrate_tuples():
    """Creating and using tuples.
    - create and print empty tuple, 1-tuple, 2-tuple, mixed-type n-tuple
    - accessing elements of a tuple using []
    - demonstrate that tuples are immutable
    """

    empty_tuple = ()
    print(type(empty_tuple))
    print(empty_tuple)
    print()

    one_tuple = 1,
    print(type(one_tuple))
    print(one_tuple)
    print()

    pair = 1, 2
    print(type(pair))
    print(pair)
    print()

    triplet = 1, 2, 'three',
    print(type(triplet))
    print(triplet)
    print()

    print(triplet[0], triplet[2])
    print()

    for i in range(len(triplet)):
        print(triplet[i])

    # triplet[2] = 3


#%%
# Test demonstrate_tuples()
demonstrate_tuples()


#%%
def demonstrate_packing():
    """Packing and unpacking tuples.
    """

    paul = 'Paul McCartney', 'Liverpool', 1942, True
    name, city, year, valid = paul
    print(paul)
    print(name, city, year, valid)
    print()

    print({name, city, year, valid})
    print(type({name, city, year, valid}))
    print(list(paul))


#%%
# Test demonstrate_packing()
demonstrate_packing()


#%%
def demonstrate_zip():
    """Using the built-in zip() function with tuples and multi-counter for-loop.
    - demonstrate zip object
    - demonstrate converting a zip object to a list object
    - demonstrate that a zip object is an iterator (must be re-initialized after looping)
    """

    members = ('John Lennon', 'Paul McCartney', 'George Harrison', 'Ringo Starr')
    birth_years = (1940, 1942, 1943, 1940)
    birth_places = ('Liverpool', 'Liverpool', 'Liverpool', 'Liverpool', )

    theBeatles = zip(members, birth_years, birth_places)
    print(list(theBeatles))
    print(theBeatles)
    for member in theBeatles:
        print(member)
    print()

    theBeatles = zip(members, birth_years, birth_places)
    print(list(theBeatles))
    theBeatles = zip(members, birth_years, birth_places)
    print(tuple(theBeatles))
    theBeatles = zip(members, birth_years, birth_places)
    print(set(theBeatles))
    print()

    theBeatles = zip(members, birth_years, birth_places)
    for name, year, city in theBeatles:
        print(f'{name} was born in {year} in {city}.')



#%%
# Test demonstrate_zip
demonstrate_zip()
