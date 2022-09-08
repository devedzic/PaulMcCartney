"""The very first Python script - main.py.
"""


# Hello world: the print() built-in function and the + operator.

print('Paul McCartney')
print('Paul McCartney', 'was born in', 1942)
#%%
# print('Paul McCartney', 'was born in', 1942 + '.')
print('Paul McCartney', 'was born in', str(1942) + '.')
print('Paul McCartney wrote \'Yesterday\' in \n' + str(1965))


#%%
# # The input() built-in function

# print('Paul McCartney was born in: ')
# year = input()
# print('Paul McCartney was born in: ', end='')
# year = input()
# print('Paul McCartney was born in:', year + '.')

# print('Paul McCartney was born in:', int(input()))


# A simple function and function call

def year_of_birth():
    print('Paul McCartney was born in: ', end='')
    year = input()
    return year

print(year_of_birth())


# A simple loop and the range() built-in function


# A simple list, accessing list elements, printing lists


# Looping through list elements - for and enumerate()


# Global variables: __name__, __file__, __doc__,...

