"""Demonstrates peculiarities of if, for, while and other statements.
"""


#%%
def demonstrate_branching():
    """Details and peculiarities of if statements.
    - is compares id()'s, == compares contents
    - id()'s are the same for equal strings and numbers, but not for lists, user class instances,...
    - the condition of an if-statement need not necessarily be a boolean
    - there can be more than one elif after if (no switch statement, use multiple elif instead)
    """

    i = [23, 23]
    j = [23, 23]
    if id(i) == id(j):
        print(True)
    else:
        print(False)
    print()

    if 4:
        print(True)
    else:
        print(False)
    print()

    n = 4
    if n == 1:
        print(1)
    elif n == 2:
        print(2)
    elif n == 3:
        print(3)
    else:
        print(None)


#%%
# Test demonstrate_branching()
demonstrate_branching()


#%%
def demonstrate_loops():
    """Different kinds of loops. Also break and continue.
    - it is not necessary to iterate through all elements of an iterable
    - step in range()
    - unimportant counter (_)
    - break and continue
    - while loop
    """

    l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    for i in l[2:-3]:
        print(i)
    print()

    for i in range(1, 12, 2):
        print(i)
    print()

    for _ in range(1, 12, 2):
        print('Sir Paul')
    print()


#%%
demonstrate_loops()
