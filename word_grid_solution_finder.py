import functools

alphabet = 'abcdefghijklmnopqrstuvwxyz'

width = 0
height = 0
grid = []

def print_grid():
    for row in grid:
        for letter in row:
            print(letter, end=" ")
        print()

# open "input.txt" and initialize  the user-input grid
with open("input.txt", 'r') as input_file:

    # read in every line from "input.txt"
    lines = input_file.readlines()

    # strip each line
    for i in range(len(lines)):
        lines[i] = lines[i].strip()

    # read the first line to find the width and height
    width_and_height = lines[0].split(' ')
    width = int(width_and_height[0])
    height = int(width_and_height[1])

    # initialize the grid with empty rows according to the width and height
    grid = [['#' for _ in range(width)] for _ in range(height)]

    # populate the grid according to the input
    row = 1
    while row <= height:
        input_row = lines[row].split(' ')
        for i in range(len(input_row)):
            grid[row - 1][i] = input_row[i]
        row += 1

