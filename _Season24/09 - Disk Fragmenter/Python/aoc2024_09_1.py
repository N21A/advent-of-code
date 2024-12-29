"""
aoc2024_09_1.py
----------------
Author: Nida Anis
Date: 28/12/2024
----------------
Description:
- Advent of Code 2024 Day 9: Disk Fragmenter
- Solution to Part 1 (Part 2 in aoc2024_09_1.py)
"""

def get_disk_map_from_file():
    """
    Reads the disk map from the file into a "disk_map" string.
    """
    disk_map = ""

    with open("input.txt", "r") as f:
        disk_map = f.read().strip()
    
    return disk_map

def parse_disk_map(disk_map):
    """
    Unpacks the disk map and returns an "unpacked_disk_map" array.
    """
    unpacked_disk_map = []
    file_id = 0

    for i in range(len(disk_map)):
        # Even numbers represent the length of a file
        if i % 2 == 0:
            length = int(disk_map[i])
            unpacked_disk_map.extend([str(file_id)] * length)
            file_id += 1
        # Odd numbers represent the length of free space
        elif i % 2 != 0:
            length = int(disk_map[i])
            unpacked_disk_map.extend(['.'] * length)
        
    return unpacked_disk_map

def defragment_disk_map(unpacked_disk_map, verbose=False):
    """
    Defragments the disk map and returns a "defrag_disk_map" array.
        -> Moves blocks instead of whole files.
    """
    defrag_disk_map = unpacked_disk_map[:]

    print("Starting disk map:", ''.join(defrag_disk_map))

    for i in range(len(defrag_disk_map) -1, -1, -1):
        if defrag_disk_map[i] != '.':
            for j in range(i):
                if defrag_disk_map[j] == '.':
                    defrag_disk_map[j], defrag_disk_map[i] = defrag_disk_map[i], defrag_disk_map[j]
                    if verbose:
                        # print(f"Moved block (File ID {defrag_disk_map[j]}) from {i} to {j}")
                        print("Updated disk map:", ''.join(defrag_disk_map))
                    break

    return defrag_disk_map

def calculate_checksum(defrag_disk_map):
    """
    Calculates the filesystem checksum by summing position * file ID.
    """
    checksum = 0

    for position, block in enumerate(defrag_disk_map):
        if block != '.':
            checksum += position * int(block)
    
    return checksum

def main():
    # Set to True to enable verbose output
    verbose = True

    disk_map = get_disk_map_from_file()
    unpacked_disk_map = parse_disk_map(disk_map)
    defrag_disk_map = defragment_disk_map(unpacked_disk_map, verbose=verbose)
    checksum = calculate_checksum(defrag_disk_map)
    print("Checksum:", checksum)

if __name__ == "__main__":
    main()