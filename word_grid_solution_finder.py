import functools

alphabet = 'abcdefghijklmnopqrstuvwxyz'

width = input("Enter the grid's width: ")
height = input("Enter the grid's height: ")
grid = []

# convert list of characters to string
# from Geeksforgeeks
def convert(s):
    # Using reduce to join the list s to string
    str1 = functools.reduce(lambda x,y : x+y, s)
    return str1

def print_grid():
    for row in grid:
        for letter in row:
            print(letter, end=" ")
        print()