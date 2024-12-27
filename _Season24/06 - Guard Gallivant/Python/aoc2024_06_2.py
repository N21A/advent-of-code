"""
aoc2024_06_2.py
----------------
Author: Nida Anis
Date: 27/12/2024
----------------
Description:
- Advent of Code 2024 Day 6: Guard Gallivant
- Solution to Part 2 (Part 1 in aoc2024_06_1.py)
"""

from aoc2024_06_1 import get_map_from_file, find_starting_coords, move_guard

# Import relevant modules
import copy

def simulate_obstruction(grid, start_pos, obstr_pos):
    """
    Simulates the guard's movement with an extra obstruction.
    If the guard gets stuck in a loop, the function returns True.
    Otherwise, the function will return False.
    """
    grid_copy = copy.deepcopy(grid) # Create a copy of the grid
    y_obstr, x_obstr = obstr_pos
    grid_copy[y_obstr][x_obstr] = '#' # Place the obstruction

    # start_pos = find_starting_coords(grid)
    visited_with_directions = set() # Track position and direction
    current_pos = start_pos

    while True:
        y, x = current_pos
        direction = grid_copy[y][x]

        # Check if we've revisited a position with the same direction
        if (current_pos, direction) in visited_with_directions:
            grid[y_obstr][x_obstr] = '.' # Reset obstruction
            return True # Loop detected!
        
        visited_with_directions.add((current_pos, direction))

        result = move_guard(grid_copy, current_pos, visited_with_directions)

        if result == True: # Guard leaves the map
            grid[y_obstr][x_obstr] = '.' # Reset obstruction
            return False
        
        elif result == False: # Guard turns in place
            continue

        else:
            current_pos = result

def find_valid_obstructions(grid, verbose=False):
    """
    Finds all positions where adding an obstruction causes the guard to get stuck.
    """
    valid_positions = set()
    start_pos = find_starting_coords(grid)

    for y in range(len(grid)):
        if verbose:
            print(f"Testing obstructions on row {y}...")
        for x in range(len(grid[0])):
            if (y, x) == start_pos or grid[y][x] == '#':
                continue # Skip starting position and existing obstructions

            if simulate_obstruction(grid, start_pos, (y, x)):
                valid_positions.add((y, x))
                if verbose:
                    print(f"    -> Valid obstruction at ({y}, {x}) (Total: {len(valid_positions)})")
                    # print(f"Number of valid obstructions:", len(valid_positions))
    
    return valid_positions

def main():
    grid = get_map_from_file()
    start_pos = find_starting_coords(grid)

    verbose = True # Set to True for verbose output
    valid_positions = find_valid_obstructions(grid, verbose=verbose)
    print("Number of valid obstructions:", len(valid_positions))

if __name__ == "__main__":
    main()