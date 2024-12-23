"""
aoc2024_03.py
----------------
Author: Nida Anis
Date: 23/12/2024
----------------
Description:
Solution to Advent of Code 2024 Day 3: Mull It Over
"""

# Import relevant modules
import re

# Implement error handling
try:
    # Open input.txt
    f = open("input.txt", "r")

    # Read input.txt into string
    text = f.read()

    # Initialise arrays
    match_start_positions = []
    flag_end_positions = []
    flag_intervals = []
    valid_matches = []

    # Initialise variables
    sum1 = 0
    sum2 = 0
    flag_enabled = True

    # Define the match regex pattern
    # mul\( - Matches literal text mul(
    # (\d+) - Matches one or more digits and captures in first group
    # , - Matches the literal comma
    # (\d+) - Matches one or more digits and captures in second group
    # \) - Matches the closing parenthesis
    match_pattern = r"mul\((\d+),(\d+)\)"

    # Define the flag regex pattern
    # do\(\) - Matches literal text do()
    # | - OR operator, allowing either pattern to match
    # don't\(\) - Matches literal text don't()
    flag_pattern = r"do\(\)|don't\(\)"

    # Find all instructions (matches and flags) in order
    instructions = []
    for match in re.finditer(match_pattern, text):
        instructions.append(("mul", int(match.start()), match.groups()))
    for flag in re.finditer(flag_pattern, text):
        instructions.append(("flag", int(flag.start()), flag.group()))

    # Sort instructions by position
    instructions.sort(key=lambda x: x[1])

    # Process instructions
    for instr_type, pos, value in instructions:
        if instr_type == "flag":
            if value == "do()":
                flag_enabled = True
            elif value == "don't()":
                flag_enabled = False

        elif instr_type == "mul":
            num1, num2 = map(int, value)
            result = num1 * num2

            # Add all results
            sum1 += result

            # Add results only if enabled
            if flag_enabled:
                sum2 += result
    
    # Print all multiplication results
    print("All multiplication results:", sum1)

    # Print only valid multiplication results
    print("Valid multiplication results:", sum2)

    # Close file
    f.close()

except FileNotFoundError:
    print("File not found.")