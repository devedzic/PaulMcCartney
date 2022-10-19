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
    s.add('Paul McCartney')
    print(type(s))
    print(s)
    s.update([1942, 'Liverpool'])
    print(s)
    s.update([1942, 'Liverpool'])
    print(s)
    s.add(1942)
    print(s)
    s = s | {1942}
    print(s)
    print()

    print(s | {'John Lennon'})
    print(s | {'John Lennon', 1942})
    print(s & {'John Lennon', 1942})
    print(s - {'John Lennon', 1942})
    print(s ^ {'John Lennon', 1942})


#%%
# Test demonstrate_sets()
demonstrate_sets()

