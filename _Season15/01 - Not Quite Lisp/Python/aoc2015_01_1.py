"""
aoc2015_01_1.py
----------------
Author: Nida Anis
Date created: 20/02/2025
----------------
Description:
- Advent of Code 2015 Day 1: Not Quite Lisp
- Solution to Part 1 (Part 2 in aoc2015_01_2.py)
"""

def get_map_from_file():
    """Reads the map from the input file."""
    map = []

    with open("input.txt", "r") as f:
        while 1:
            char = f.read(1)
            map.append(char)
            if not char:
                break
    
    return map

def get_final_floor_number(map):
    """Gets Santa's final floor number."""
    floor_num = 0

    for char in map:
        if char == "(":
            floor_num += 1

        elif char == ")":
            floor_num -= 1
    
    return floor_num

def main():
    map = get_map_from_file()
    floor_num = get_final_floor_number(map)
    print(f"The instructions take Santa to Floor {floor_num}.")

if __name__ == "__main__":
    main()