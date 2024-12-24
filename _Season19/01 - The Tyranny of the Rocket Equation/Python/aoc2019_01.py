"""
aoc2019_01.py
----------------
Author: Nida Anis
Date: 23/12/2024
----------------
Description:
Solution to Advent of Code 2019 Day 1: The Tyranny of the Rocket Equation
"""

# Import relevant modules
import math

try:

    # Open file
    f = open("input.txt")

    # Initialise variables
    fuel_required = 0
    fuel_total = 0

    # Iterate over each mass in the file
    for mass in f:
        fuel_required = math.floor((int(mass) / 3)) - 2
        fuel_total += fuel_required

    # Print the sum of the fuel requirements
    print("The sum of the fuel requirements is:", fuel_total)

    # Close file
    f.close()

except FileNotFoundError:
    print("File not found.")