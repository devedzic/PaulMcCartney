"""Demonstrates sets.
"""


#%%
def demonstrate_sets():
    """Creating and using sets.
    - create a set and make an attempt to duplicate items
    - demonstrate some typical set operators:
        & (intersection)
        | (union)
        - (difference)
        ^ (disjoint)
    """

    s = set()
    print(type(s))
    print(s)
    print()

    s.add('Paul McCartney')
    print(s)
    print()

    s.update(['Liverpool', 1942])
    print(s)
    print()
    s.update(['Liverpool', 1942])
    print(s)
    print()
    s.add(1942)
    print(s)
    print()

    s = s | {'John Lennon', 1940}
    print(s)
    print(s & {'Paul McCartney'})
    print(s - {'Paul McCartney'})
    print(s ^ {'Paul McCartney'})


#%%
# Test demonstrate_sets()
demonstrate_sets()

