"""
aoc2024_02.py
----------------
Author: Nida Anis
Date: 22/12/2024
----------------
Description:
Solution to Advent of Code 2024 Day 2: "Red-Nosed Reports".
""" 

# Implement error handling
try:
    # Open input.txt
    f = open("input.txt", "r")

    reports = []

    # Read the file into a two-dimensional array
    for line in f:
        reports.append([int(num) for num in line.strip().split()])

    # Initialise number of safe reports
    safe_reports = 0

    # Initialise problem dampener
    problem_dampener = []

    for report in reports:
        # Calculate the differences between adjacent levels
        differences = [report[i+1] - report[i] for i in range(len(report) - 1)]

        # 01: Check for a consistent increase or decrease
        is_increasing = all(diff > 0 for diff in differences)
        is_decreasing = all(diff < 0 for diff in differences)

        # 02: Check if differences are within the valid range
        valid_differences = all(1 <= abs(diff) <= 3 for diff in differences)

        if valid_differences and (is_increasing or is_decreasing):
            safe_reports += 1

        else:
    
            # 03: Use the Problem Dampener
            for i in range(len(report)):
                problem_dampener = report[:i] + report[i+1:]
                differences = [problem_dampener[j+1] - problem_dampener[j] for j in range(len(problem_dampener) - 1)]

                # 03.01: Check for a consistent increase or decrease
                is_increasing = all(diff > 0 for diff in differences)
                is_decreasing = all(diff < 0 for diff in differences)

                # 03.02: Check if differences are within the valid range
                valid_differences = all(1 <= abs(diff) <= 3 for diff in differences)

                if valid_differences and (is_increasing or is_decreasing):
                    safe_reports += 1
                    break

    print("The number of safe reports is:", safe_reports)

    # Close file
    f.close()

except FileNotFoundError:
    print("File not found.")