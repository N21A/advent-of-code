"""
aoc2024_11_2.py
----------------
Author: Nida Anis
Date: 29/12/2024
----------------
Description:
- Advent of Code 2024 Day 11: Plutonian Pebbles
- Solution to Part 2 (Part 11 in aoc2024_11_1.py)
"""
from collections import Counter

def get_arrangement_from_file():
    """
    Gets the initial arrangement from the input.txt file.
    """
    with open("input.txt", "r") as f:
        return list(map(int, f.read().strip().split()))

def blink_stones(arrangement, blinks):
    """
    Processes stones over a given number of blinks.
    Uses Counter for efficiency.
    """
    # Use Counter for efficient stone management
    stone_counter = Counter(arrangement)

    for blink in range(1, blinks + 1):
        new_stones = Counter()

        for stone, qty in stone_counter.items():
            if stone == 0:
                new_stones[1] += qty

            elif len(str(stone)) % 2 == 0:
                full = str(stone)
                left = int(full[:len(full)//2])
                right = int(full[len(full)//2:])
                new_stones[left] += qty
                new_stones[right] += qty
            
            else:
                new_stones[stone * 2024] += qty
            
        stone_counter = new_stones

        # Optional: Log progress
        print(f"Completed blink {blink} of {blinks}...")
        # print(f"Completed blink {blink}. Number of stones: {sum(stone_counter.values())}")
    
    return sum(stone_counter.values())

def main():
    # Set number of blinks
    blinks = 20000

    initial_arrangement = get_arrangement_from_file()
    number_of_stones = blink_stones(initial_arrangement, blinks)

    print("Number of stones:", number_of_stones)

if __name__ == "__main__":
    main()