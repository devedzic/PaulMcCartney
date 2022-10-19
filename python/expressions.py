"""Demonstrates how operators and expressions work in Python.
"""

from settings import *


#%%
def demonstrate_arithmetic_operators():
    """Working with arithmetic operators.
    Arithmetic operators in Python are pretty much the same as in other programming languages.
    The integer division operator: //
    """

    print(23 // 5 + 13 % 7 - 2**3)


#%%
# Test demonstrate_arithmetic_operators()
demonstrate_arithmetic_operators()


#%%
def demonstrate_relational_operators():
    """Working with relational operators.
    - simple comparisons
    - comparing dates (== vs. is)
    - comparing dates (>, <, etc. with dates)
    - None in comparisons, type(None)
    """

    print(2 > 3)
    print()

    if '':
        print(True)
    else:
        print(False)
    print()

    from datetime import date
    d1 = date(1942, 6, 18)
    d2 = date.today()
    print(d1 == d2)
    print(d2 is date.today())
    print('id(d1):', id(d1))
    print('id(date.today()):', id(date.today()))
    print(d2 == date.today())
    print()

    print(None)
    print(None == 2)
    print(type(2))
    print(type(None))
    print(not None)
    print()


#%%
# Test demonstrate_relational_operators()
demonstrate_relational_operators()


#%%
def demonstrate_logical_operators():
    """Working with logical operators.
    - logical operations with True, False and None
    - logical operations with dates
        - make sure to read this: https://docs.python.org/3/library/stdtypes.html#boolean-operations-and-or-not !!!
          (or just this: https://stackoverflow.com/questions/44612144/logical-operators-in-python)
    - logical operations with None (incl. None and int, None and date, etc.)
    - None and date vs. None > date
    """

    print(True and None)
    print(True or None)
    print(True and not None)
    print()

    print(1 and 5)
    print('' and 5)
    print()

    from datetime import date
    d1 = date.today()
    print(d1 and None)
    print(d1 and not None)
    # print(d1 > None)


#%%
# Test demonstrate_logical_operators()
demonstrate_logical_operators()

