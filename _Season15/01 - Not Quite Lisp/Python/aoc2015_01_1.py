"""
aoc2015_01_1.py
----------------
Author: Nida Anis
Date: 22/12/2024
- Revised 31/12/2024
----------------
Description:
- Advent of Code 2015 Day 1: Not Quite Lisp
- Solution to Part 1 (Part 2 in aoc2015_01_2.py)
"""

def get_map_from_file():
    """
    Reads the map from the input file.
    """
    map = []

    with open("input.txt", "r") as f:
        # Read each character into the map
        while 1:
            char = f.read(1)
            map.append(char)
            if not char:
                break
    
    return map

def get_final_floor_number(map):
    """
    Gets Santa's final floor number.
    """
    floor_count = 0

    for char in map:

        if char == "(":
            floor_count += 1
        
        elif char == ")":
            floor_count -= 1
    
    return floor_count

def main():
    map = get_map_from_file()
    floor_count = get_final_floor_number(map)
    print("Advent of Code 2015 Day 1: Not Quite Lisp")
    print(f"Running Part 1...")
    print(f"The instructions take Santa to Floor {floor_count}.")

if __name__ == "__main__":
    main()