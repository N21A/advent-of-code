"""
aoc2024_11_1.py
----------------
Author: Nida Anis
Date: 29/12/2024
----------------
Description:
- Advent of Code 2024 Day 11: Plutonian Pebbles
- Solution to Part 1 (Part 2 in aoc2024_11_2.py)
"""
from collections import deque

def get_arrangement_from_file():
    """
    Gets the initial arrangement from the input.txt file.
    """
    initial_arrangement = []

    with open("input.txt", "r") as f:
        initial_arrangement = f.read().split()
        initial_arrangement = [int(x) for x in initial_arrangement]
    
    return initial_arrangement

def split_number(number):
    """
    Splits a number into two halves.
    Returns two integers: left_half and right_half.
    """
    str_num = str(number)
    mid = len(str_num) // 2
    return int(str_num[:mid]), int(str_num[mid:])

def blink_stones(blinks, initial_arrangement):
    """
    Processes stones over the given number of blinks.
    """
    arrangement = deque(initial_arrangement)

    for i in range(blinks):
        print(f"Calculating blink {i + 1} of {blinks}...")
        new_arrangement = deque()
    
        while arrangement:
            stone = arrangement.popleft()
            if stone == 0:
                new_arrangement.append(0)

            elif len(str(stone)) % 2 == 0 and stone != 0:
                left, right = split_number(stone)
                new_arrangement.append(left)
                new_arrangement.append(right)

            else:
                new_arrangement.append(stone * 2024)
        
        arrangement = new_arrangement
        print(f"Completed blink {i + 1}. Number of stones: {len(arrangement)}")
    
    return list(arrangement)

def main():
    # Set number of blinks
    blinks = 25

    initial_arrangement = get_arrangement_from_file()
    print("Initial arrangement:", initial_arrangement)
    arrangement = blink_stones(blinks, initial_arrangement)
    print("Number of stones:", len(arrangement))

if __name__ == "__main__":
    main()