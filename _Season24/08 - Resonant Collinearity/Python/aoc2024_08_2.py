"""
aoc2024_08_2.py
----------------
Author: Nida Anis
Date: 28/12/2024
----------------
Description:
- Advent of Code 2024 Day 8: Resonant Collinearity
- Solution to Part 2 (Part 1 in aoc2024_08_1.py)
"""

from aoc2024_08_1 import get_map_from_file, parse_map

def is_collinear(x1, y1, x2, y2, x3, y3):
    """
    Checks if three points (x1, y1), (x2, y2), and (x3, y3) are collinear.
    """
    return (x2 - x1) * (y3 - y1) == (y2 - y1) * (x3 - x1)

def find_antinodes(antennas, width, height):
    """
    Determines all unique antinode locations caused by antenna pairs, regardless of distance.
        -> Returns a set of unique (x, y) coordinates representing antinodes.
    """
    antinode_set = set()

    valid_antinode_count = 0

    for i, antenna1 in enumerate(antennas):
        for j, antenna2 in enumerate(antennas):
            # Avoid redundant pair evaluations
            # Ensure only matching pairs are evaluated:
            if i >= j or antenna1[2] != antenna2[2]:
                continue

            for x in range(width):
                for y in range(height):
                    # Check if (x, y) is collinear with the two antennas
                    if is_collinear(antenna1[0], antenna1[1], antenna2[0], antenna2[1], x, y):
                        if 0 <= x < width and 0 <= y < height:
                            valid_antinode_count += 1
                            antinode_set.add((x, y))
                            print(f"    -> Valid antinode found! ({x}, {y}) (Total: {valid_antinode_count})")
            
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