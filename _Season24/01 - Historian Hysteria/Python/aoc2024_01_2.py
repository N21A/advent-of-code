"""
aoc2024_01_2.py
----------------
Author: Nida Anis
Date created: 21/02/2025
----------------
Description:
- Advent of Code 2024 Day 1: "Historian Hysteria"
- Solution to Part 2 (Part 1 in aoc2024_01_1.py)
"""

from aoc2024_01_1 import get_input_from_file

def calc_similarity_sum(list1, list2):
    """Calculates the sum of the similarity scores between items in the two lists."""
    count = 0
    similarity_sum = 0
    similarity_scores = []

    for i in range(0, len(list1)):
        for j in range(0, len(list2)):
            if list1[i] == list2[j]:
                count += 1
        similarity_scores.append(int(list1[i]) * count)
        count = 0
    
    for i in range(0, len(similarity_scores)):
        similarity_sum += similarity_scores[i]

    return similarity_sum

def main():
    list1, list2 = get_input_from_file()
    similarity_sum = calc_similarity_sum(list1, list2)
    print("Sum of similarity scores:", similarity_sum)

if __name__ == "__main__":
    main()
