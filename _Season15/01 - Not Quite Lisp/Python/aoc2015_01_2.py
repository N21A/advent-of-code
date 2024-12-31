"""
aoc2015_01_2.py
----------------
Author: Nida Anis
Date: 31/12/2024
----------------
Description:
- Advent of Code 2015 Day 1: Not Quite Lisp
- Solution to Part 2 (Part 1 in aoc2015_01_1.py)
"""
from aoc2015_01_1 import get_map_from_file

def get_first_basement_pos(map):
    """
    Get the position of the character that causes Santa to first enter the basement.
    """
    pos = 0
    floor_count = 0
    basement_pos = []

    for char in map:
        pos += 1

        if char == "(":
            floor_count += 1
        
        elif char == ")":
            floor_count -= 1
        
        if floor_count == -1:
            basement_pos.append(pos)
    
    return basement_pos

def main():
    map = get_map_from_file()
    basement_pos = get_first_basement_pos(map)
    print("Advent of Code 2015 Day 1: Not Quite Lisp")
    print(f"Running Part 2...")
    print(f"The position of the character that causes Santa to first enter the basement is {basement_pos[0]}.")

if __name__ == "__main__":
    main()