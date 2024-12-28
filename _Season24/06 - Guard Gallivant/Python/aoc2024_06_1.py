"""
aoc2024_06_1.py
----------------
Author: Nida Anis
Date: 26/12/2024
----------------
Description:
- Advent of Code 2024 Day 6: Guard Gallivant
- Solution to Part 1 (Part 2 in aoc2024_06_2.py)
"""

def get_map_from_file():
    """
    Gets map information from the input file.
    Returns this information in the two-dimensional "grid" array.
    """
    grid = []

    with open("input.txt", "r") as f:
        for line in f.readlines():
            grid.append([char for char in line if char != '\n'])

    return grid

def find_starting_coords(grid):
    """
    Finds the guard's starting coordinates on the grid.
    Returns the y- and x-values of these coordinate.
    """
    for y, line in enumerate(grid):
        for x, char in enumerate(line):
            if char in "^>v<":
                return y, x

def check_cells_ahead(grid, current_pos):
    y, x = current_pos
    direction = grid[y][x]
    is_clear = False
    is_boundary = False

    match direction:
        case '^':
            # Case for ^
            if y == 0:
                is_boundary = True
            elif grid[y-1][x] == '.':
                    is_clear = True

        case '>':
            # Case for >
            if x == (len(grid[0])) - 1:
                is_boundary = True
            elif grid[y][x+1] == '.':
                    is_clear = True
        
        case 'v':
            # Case for v
            if y == len(grid) - 1:
                is_boundary = True
            elif grid[y+1][x] == '.':
                    is_clear = True
        
        case '<':
            # Case for <
            if x == 0:
                is_boundary = True
            elif grid[y][x-1] == '.':
                    is_clear = True

    return direction, is_clear, is_boundary

def update_pos(x, y):
    """
    Updates the position of the guard.
    """
    return (x, y)

def move_guard(grid, current_pos, visited):
    y, x = current_pos
    direction = grid[y][x]
    new_y, new_x = y, x

    # Determine movement based on direction
    match direction:
        case '^':
            new_y -= 1
        case '>':
            new_x += 1
        case 'v':
            new_y += 1
        case '<':
            new_x -= 1
    
    # Check for boundaries
    if new_y < 0 or new_y >= len(grid) or new_x < 0 or new_x >= len(grid[0]):
        return True # Guard leaves the map
    
    if grid[new_y][new_x] == '#':
        # Turn right 90 degrees
        match direction:
            case '^':
                grid[y][x] = '>'
            case '>':
                grid[y][x] = 'v'
            case 'v':
                grid[y][x] = '<'
            case '<':
                grid[y][x] = '^'
        return False # Guard stays in place
    
    # Move guard forward
    grid[y][x] = 'X'
    grid[new_y][new_x] = direction
    visited.add((new_y, new_x))
    return (new_y, new_x)

def main():
    grid = get_map_from_file()
    start_pos = find_starting_coords(grid)
    visited = {start_pos}

    current_pos = start_pos

    while True:
        result = move_guard(grid, current_pos, visited)
        if result == True:
            break
        elif result == False:
            continue
        else:
            current_pos = result

    print("Distinct positions visited:", len(visited))

if __name__ == "__main__":
    main()