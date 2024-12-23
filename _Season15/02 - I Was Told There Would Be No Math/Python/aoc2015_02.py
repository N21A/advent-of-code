"""
aoc2015_02.py
----------------
Author: Nida Anis
Date: 23/12/2024
----------------
Description:
Solution to Advent of Code 2015 Day 2: "I Was Told There Would Be No Math
"""

# Import relevant modules
import re

try:
    # Open input.txt
    f = open("input.txt", "r")

    # Declare arrays
    dimensions = []
    presents = []

    # Declare variables
    sum = 0
    total_wrap = 0

    # Define the regex pattern used to extract integers
    pattern = r"(\d+)x(\d+)x(\d+)"

    # Read each line into the dimensions array
    for line in f:
        dimensions.append(line.strip())

        for present in re.finditer(pattern, line):
            presents.append((present.groups()))
    
    for value in presents:
        sides = []
        l, w, h = map(int, value)

        # 01: Calculate surface area of box
        surface_area = 2*l*w + 2*w*h + 2*h*l

        # 02: Calculate the smallest side
        sides = [l*w, w*h, h*l]
        smallest_side = min(sides)

        # 03: Calculate wrap_needed
        wrap_needed = surface_area + smallest_side

        total_wrap += wrap_needed

    print("Total wrap required:", total_wrap, "square feet")


    # Close the file
    f.close()

except FileNotFoundError:
    print("File not found.")