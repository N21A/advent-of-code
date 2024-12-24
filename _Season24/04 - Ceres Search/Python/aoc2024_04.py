"""
aoc2024_04.py
----------------
Author: Nida Anis
Date: 24/12/2024
----------------
Description:
Solution to Advent of Code 2024 Day 4: Ceres Search
"""

# Import relevant modules
import numpy as np

try:
    # Open file
    f = open("input.txt", "r")

    """
    Day 4 - Part 1
    """

    # Initialise arrays
    d = []
    d_flipped = []

    # Horizontal instances:

    # Read each line into the lines list
    lines = [line.strip() for line in f]
    # Count instances of "XMAS" and "SAMX" in each line
    h_count = [line.count("XMAS") + line.count("SAMX") for line in lines]
    # Sum the horizontal counts
    h_total = sum(h_count)

    # Vertical instances:

    # Convert the lines list into a two-dimensional array
    arr = np.array([list(line) for line in lines])
    # Transpose the array
    arr_transposed = arr.transpose()
    # Join the characters in each line together
    v_lines = ["".join(line) for line in arr_transposed]
    # Count instances of "XMAS" and "SAMX" in each line
    v_count = [line.count("XMAS") + line.count("SAMX") for line in v_lines]
    # Sum the vertical counts
    v_total = sum(v_count)

    # Diagonal instances:

    # Normal diagonals
    for i in range(-len(arr) + 1, len(arr) - 1):
        line = "".join(np.diagonal(arr, i))
        d.append(line)

    # Flipped diagonals
    for i in range (-len(arr) + 1, len(arr) - 1):
        line = "".join(np.diagonal(np.fliplr(arr), i))
        d_flipped.append(line)

    # Count the diagonal instances
    d_count = [line.count("XMAS") + line.count("SAMX") for line in d]
    d_count_flipped = [line.count("XMAS") + line.count("SAMX") for line in d_flipped]

    # Sum the diagonal counts
    d_total = sum(d_count) + sum(d_count_flipped)

    # Sum all the counts to get the answer
    t_count = h_total + v_total + d_total
    # Print the answer
    print("The first answer is:", t_count)

    """
    Day 4 - Part 2
    """

    # Define all possible X-MAS 
    xmas_1 = (['M', '.', 'M'],
              ['.', 'A', '.'],
              ['S', '.', 'S'])

    xmas_2 = (['S', '.', 'S'],
              ['.', 'A', '.'],
              ['M', '.', 'M'])
    
    xmas_3 = (['M', '.', 'S'],
              ['.', 'A', '.'],
              ['M', '.', 'S'])
    
    xmas_4 = (['S', '.', 'M'],
              ['.', 'A', '.'],
              ['S', '.', 'M'])
    
    # Initialise variables
    xmas_count = 0

    for i in range(len(arr) - 2):
        for j in range(len(arr) - 2):
            box = arr[j:j+3, i:i+3].copy()
            # Replace irrelevant characters with '.'
            box[0][1] = '.'
            box[1][0] = '.'
            box[1][2] = '.'
            box[2][1] = '.'

            # Perform an element-wise comparison
            # If the box matches an X-MAS combination, +1
            if (box == xmas_1).sum() == 9:
                xmas_count += 1
            if (box == xmas_2).sum() == 9:
                xmas_count += 1
            if (box == xmas_3).sum() == 9:
                xmas_count += 1
            if (box == xmas_4).sum() == 9:
                xmas_count += 1
            
    print("The second answer is:", xmas_count)

    # Close file
    f.close()

except FileNotFoundError:
    print("File not found.")