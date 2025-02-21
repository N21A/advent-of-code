"""
aoc2024_01_1.py
----------------
Author: Nida Anis
Date created: 21/02/2025
----------------
Description:
- Advent of Code 2024 Day 1: "Historian Hysteria"
- Solution to Part 1 (Part 2 in aoc2024_01_2.py)
"""

def get_input_from_file():
    """Reads the puzzle input into two sorted lists."""
    list1 = []
    list2 = []

    with open ("input.txt", "r") as f:
        for line in f:
            row = line.split()
            list1.append(row[0])
            list2.append(row[1])
            list1.sort()
            list2.sort()
    
    return (list1, list2)

def calc_distance_sum(list1, list2):
    """Calculates the sum of the distances between items in the two lists."""
    distance_sum = 0
    distances = []

    for i in range(0, len(list1)):
        distances.append(abs(int(list1[i])-int(list2[i])))
    
    for i in range(0, len(distances)):
        distance_sum += distances[i]
    
    return distance_sum

def main():
    list1, list2 = get_input_from_file()
    distance_sum = calc_distance_sum(list1, list2)
    print("Sum of distances:", distance_sum)

if __name__ == "__main__":
    main()
