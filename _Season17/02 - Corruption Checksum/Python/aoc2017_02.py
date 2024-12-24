"""
aoc2017_02.py
----------------
Author: Nida Anis
Date: 23/12/2024
----------------
Description:
Solution to Advent of Code 2017 Day 02: Corruption Checksum
"""

try:
    # Open file
    f = open("input.txt", "r")

    # Initialise variables
    largest = 0
    smallest = 0
    difference = 0
    checksum = 0

    # Initialise arrays
    spreadsheet = []

    # Read the file into a two-dimensional array
    for line in f:
        spreadsheet.append([int(num) for num in line.strip().split()])

    # Iterate over each row in the spreadsheet
    for row in spreadsheet:
        largest = max(row)
        smallest = min(row)
        difference = largest - smallest
        checksum += difference

    # Print the checksum
    print("The checksum is:", checksum)

    # Close file
    f.close()

except FileNotFoundError:
    print("File not found.")