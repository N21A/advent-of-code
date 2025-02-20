"""
aoc2015_01_1.py
----------------
Author: Nida Anis
Date created: 20/02/2025
----------------
Description:
- Advent of Code 2015 Day 1: Not Quite Lisp
- Solution to Part 2 (Part 1 in aoc2015_01_1.py)
"""

from aoc2015_01_1 import get_map_from_file

def get_first_basement_pos(map):
    """Gets the first position of the character that causes Santa to enter the basement."""
    position = 0
    floor_num = 0
    basement_positions = []

    for char in map:
        position += 1

        if char == "(":
            floor_num += 1
        
        elif char == ")":
            floor_num -= 1
        
        if floor_num == -1:
            basement_positions.append(position)
    
    return basement_positions

def main():
    map = get_map_from_file()
    basement_positions = get_first_basement_pos(map)
    print(f"The position of the first character that causes Santa to enter the basement is {basement_positions[0]}.")

if __name__ == "__main__":
    main()