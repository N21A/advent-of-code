"""
aoc2024_08_1.py
----------------
Author: Nida Anis
Date: 28/12/2024
----------------
Description:
- Advent of Code 2024 Day 8: Resonant Collinearity
- Solution to Part 1 (Part 2 in aoc2024_08_2.py)
"""

def get_map_from_file():
    """
    Gets map information from the input file.
    Returns this information in the two-dimensional "grid" array.
    """
    grid = []

    with open("input.txt", "r") as f:
        for line in f.readlines():
            grid.append([char for char in line.strip()])
    
    return grid

def parse_map(grid):
    """
    Parses the input map to identify the positions and frequencies of the antennas.
        -> Iterates through each line (y) and character (x) in the input map.
        -> If a character is not a dot (.), it is recognised with an antenna with a specific frequency.
        -> Collects the antenna's coordinates (x, y) and its frequency (character) in a list.
    """
    antennas = []
    for y, line in enumerate(grid):
        for x, char in enumerate(line):
            if char != '.':
                antennas.append((x, y, char))

    return antennas

def find_antinodes(antennas, width, height):
    """
    Determines all unique antinode locations caused by antenna pairs.
        -> Returns a set of unique (x, y) coordinates representing antinode locations.
    """
    antinode_set = set()

    for i, antenna1 in enumerate(antennas):
        for j, antenna2 in enumerate(antennas):
            # Avoid redundant pair evaluations
            # Ensure only matching pairs are evaluated:
            if i >= j or antenna1[2] != antenna2[2]:
                continue

            dx = antenna2[0] - antenna1[0]
            dy = antenna2[1] - antenna1[1]

            # Check for antinodes twice as far
            antinode1 = (antenna1[0] - dx, antenna1[1] - dy)
            antinode2 = (antenna2[0] + dx, antenna2[1] + dy)

            for antinode in (antinode1, antinode2):
                x, y = antinode
                if 0 <= x < width and 0 <= y < height:
                    antinode_set.add((x, y))

    return antinode_set

def main():
    grid = get_map_from_file()
    antennas = parse_map(grid)

    width = len(grid[0])
    height = len(grid)

    antinodes = find_antinodes(antennas, width, height)

    print("Number of unique antinode locations:", len(antinodes))

if __name__ == "__main__":
    main()