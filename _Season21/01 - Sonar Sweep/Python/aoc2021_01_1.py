"""
aoc2021_01_1.py
----------------
Author: Nida Anis
Date: 08/02/2025
----------------
Description:
- Advent of Code 2021 Day 1: Sonar Sweep
- Solution to Part 1 (Part 2 in aoc2021_01_2.py)
"""

def get_measurements_from_file():
    """Gets the measurements from the input file."""
    measurements = []

    with open("input.txt", "r") as f:
        measurements = f.read().split()
        measurements = [int(i) for i in measurements]
    
    return measurements

def count_measurement_increases(measurements):
    """Count the number of measurement increases."""
    increases = 0

    for i in range(0, len(measurements)):
        if i == 0:
            continue

        if measurements[i] - measurements[i-1] > 0:
            increases += 1
    
    return increases

def main():
    measurements = get_measurements_from_file()
    increases = count_measurement_increases(measurements)

    print(f"The number of measurement increases is: {increases}")
    

if __name__ == main():
    main()