"""
aoc2015_01.py
----------------
Author: Nida Anis
Date: 22/12/2024
----------------
Description:
Solution to Advent of Code 2015 Day 1: "Not Quite Lisp"
"""

# Implement error handling
try:
    # Open input.txt
    f = open("input.txt", "r")

    # Initialise arrays
    sequence = []
    basement_positions = []

    # Initialise variables
    floor_counter = 0
    position = 0
    first_basement = 0

    # Read each character into the array
    while 1:
        char = f.read(1)
        sequence.append(char)
        if not char:
            break

    for char in sequence:

        positions = positions + 1

        if char == "(":
            floor_counter += 1

        elif char == ")":
            floor_counter -= 1
            
        if floor_counter == -1:
            basement_positions.append(position)

        position = position + 1

    # Find the first occurrence of Santa entering the basement
    first_basement = basement_positions[0]
    
    # Print Santa's final floor number
    print("Floor:", floor_counter)

    # Print the first occurrence of Santa entering the basement
    print("Basement position:", first_basement)

    # Close file
    f.close()

# File not found error message
except FileNotFoundError:
    print("File not found.")