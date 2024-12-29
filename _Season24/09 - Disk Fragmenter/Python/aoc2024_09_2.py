"""
aoc2024_09_2.py
----------------
Author: Nida Anis
Date: 29/12/2024
----------------
Description:
- Advent of Code 2024 Day 9: Disk Fragmenter
- Solution to Part 2 (Part 1 in aoc2024_09_1.py)
"""

from aoc2024_09_1 import get_disk_map_from_file, parse_disk_map, calculate_checksum

def defragment_disk_map(unpacked_disk_map, verbose=False):
    """
    Defragments the disk map and returns a "defrag_disk_map" array.
        -> Moves whole files instead of blocks.
    """
    defrag_disk_map = unpacked_disk_map[:]
    files = {}

    for i, block in enumerate(defrag_disk_map):
        if block != '.':
            file_id = int(block)
            if file_id not in files:
                files[file_id] = []
            files[file_id].append(i)
    
    for file_id in sorted(files.keys(), reverse=True):
        file_positions = files[file_id]
        file_length = len(file_positions)

        free_space_start = -1
        free_space_length = 0

        for i in range(len(defrag_disk_map)):
            if defrag_disk_map[i] == '.':
                if free_space_start == -1:
                    free_space_start = i
                free_space_length += 1
                free_space_end = free_space_start + free_space_length - 1
                if free_space_length >= file_length:
                    break
            
            else:
                free_space_start = -1
                free_space_length = 0
            
        if free_space_start is not -1 and free_space_length >= file_length and free_space_end < file_positions[0]:

            for pos in file_positions:
                defrag_disk_map[pos] = '.'
        
            for offset in range(file_length):
                defrag_disk_map[free_space_start + offset] = str(file_id)
            
            if verbose:
                print(f"Moved (File ID {file_id}) from position {free_space_start} to position {free_space_start + file_length - 1})")

    return defrag_disk_map

def main():
    # Set to True for verbose output
    verbose = True

    disk_map = get_disk_map_from_file()
    unpacked_disk_map = parse_disk_map(disk_map)
    defrag_disk_map = defragment_disk_map(unpacked_disk_map, verbose=verbose)
    checksum = calculate_checksum(defrag_disk_map)
    print("Checksum:", checksum)
    

if __name__ == "__main__":
    main()