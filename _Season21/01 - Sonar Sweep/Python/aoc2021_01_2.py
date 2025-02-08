"""
aoc2021_01_2.py
----------------
Author: Nida Anis
Date: 08/02/2025
----------------
Description:
- Advent of Code 2021 Day 1: Sonar Sweep
- Solution to Part 2 (Part 1 in aoc2021_01_1.py)
"""

from aoc2021_01_1 import get_measurements_from_file, count_array_increases

def get_window_sums(measurements):
    window_sums = []
    
    for i in range(0, len(measurements)):
        if i + 2 == len(measurements):
            break
        
        window_sum = measurements[i] + measurements[i+1] + measurements[i+2]
        window_sums.append(window_sum)

        if i == 0:
            continue

    return window_sums

def main():
    measurements = get_measurements_from_file()
    window_sums = get_window_sums(measurements)
    increases = count_array_increases(window_sums)
    print(f"The number of window increases is: {increases}")

if __name__ == "__main__":
    main()