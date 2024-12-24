"""
aoc2016_03.py
----------------
Author: Nida Anis
Date: 01/12/2024
----------------
Description:
Solution to Advent of Code 2016 Day 3: Squares with Three Sides
"""

try:
    # Open input.txt
    f = open("input.txt", "r")

    # Initialise variables
    is_valid = False
    count = 0

    # Read the file and process each line
    for line in f:
        # Convert the line into a tuple of three integers
        triangle = tuple(map(int, line.split()))

        # Check if the triangle is valid
        if (triangle[0] + triangle[1]) > triangle[2]:
            if (triangle[0] + triangle[2]) > triangle[1]:
                if (triangle[1] + triangle[2] > triangle[0]):
                    is_valid = True
        
        if is_valid == True:
            count += 1

        is_valid = False
    
    print("Number of possible triangles:", count)



except FileNotFoundError:
    print("File not found.")