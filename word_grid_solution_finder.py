import copy
import functools

alphabet = 'abcdefghijklmnopqrstuvwxyz'

width = 0
height = 0
crossword_grid = []
grid_solutions = []

"""
Prints the crossword grid by row
"""
def print_grid():
    for row in crossword_grid:
        for letter in row:
            print(letter, end=" ")
        print()
        
"""
Converts a list of characters to a string
From Geeksforgeeks.org
"""
def convert(s):
    # Using reduce to join the list s to string
    str1 = functools.reduce(lambda x,y : x+y, s)
    return str1

# create dictionary of every scrabble word
words_dict = {}
with open("scrabble.txt", 'r') as file:
    lines = file.readlines()
    for word in lines:
        word = word.strip().lower()
        words_dict[word] = 1

# open "input.txt" and initialize  the user-input crossword grid
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

    # initialize the crossword grid with empty rows according to the width and height
    crossword_grid = [['#' for _ in range(width)] for _ in range(height)]

    # populate the crossword grid according to the input
    row = 1
    while row <= height:
        input_row = lines[row].split(' ')
        for i in range(len(input_row)):
            crossword_grid[row - 1][i] = input_row[i]
        row += 1

"""
Recursively finds solutions to the input crossword grid
"""
def find_solutions(row, col, grid):

    # base case: the grid is full, so it is a solution
    if row == height:
        grid_solutions.append(grid)

    # base case: the row and col position aren't blank, so skip
    elif grid[row][col] != '.':

        # if the row and col position is at the end of a row, go to the next row
        if col >= width - 1:
            find_solutions(row + 1, 0, grid)

        # else, go to the next col    
        else:
            find_solutions(row, col + 1, grid)

    else:
        temp_grid = copy.deepcopy(grid)

        # iterate through each letter in the alphabet and put it in that position
        for letter in alphabet:
            temp_grid[row][col] = letter

            # check if the across word is either unfinished or invalid
            across_is_valid = True
            if col == width - 1 or temp_grid[row][col + 1] == '#':

                curr_col = col
                while curr_col >= 0:

                    # if this is the end of the row, check if the word is in the scrabble dictionary
                    if temp_grid[row][curr_col] == '#':
                        
                        # if the word is only one character long, it shouldn't be checked
                        if col - curr_col > 1:
                            across_is_valid = convert(temp_grid[row][curr_col + 1 : col + 1]) in words_dict
                    
                    elif curr_col == 0:
                        
                        # if the word is only one character long, it shouldn't be checked
                        if col - curr_col >= 1:
                            across_is_valid = convert(temp_grid[row][curr_col : col + 1]) in words_dict

                    curr_col -= 1
            
            if not across_is_valid:
                continue

            # check if the down word is either unfinished or invalid
            down_is_valid = True
            if row == height - 1 or temp_grid[row + 1][col] == '#':

                curr_row = row
                while curr_row >= 0:

                    # if this is the end of the column, check if the word is in the scrabble dictionary
                    if temp_grid[curr_row][col] == '#':
                        
                        # if the word is only one character long, it shouldn't be checked
                        if row - curr_row > 1:

                            column = []
                            for r in range(curr_row + 1, row + 1):
                                column.append(temp_grid[r][col])

                            down_is_valid = convert(column) in words_dict
                    
                    elif curr_row == 0:

                        # if the word is only one character long, it shouldn't be checked
                        if row - curr_row >= 1:

                            column = []
                            for r in range(curr_row, row + 1):
                                column.append(temp_grid[r][col])

                            down_is_valid = convert(column) in words_dict

                    curr_row -= 1
            
            if down_is_valid:
                if col >= width - 1:
                    find_solutions(row + 1, 0, copy.deepcopy(temp_grid)) 
                else:
                    find_solutions(row, col + 1, copy.deepcopy(temp_grid))

find_solutions(0, 0, crossword_grid)

with open("result.txt", 'w') as result_file:
    result_file.write("Solutions: " + str(len(grid_solutions)) + "\n\n")

    for grid in grid_solutions:
        for row in grid:
            for char in row:
                result_file.write(char + ' ')
            result_file.write('\n')
        result_file.write('\n')