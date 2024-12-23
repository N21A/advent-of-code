"""
aoc2024_01.py
----------------
Author: Nida Anis
Date: 01/12/2024
----------------
Description:
Solution to Advent of Code 2024 Day 1: "Historian Hysteria".
""" 

# Implement error handling
try:
    # Open input.txt
    f = open("input.txt", "r")
    
    # Declare lists
    list1 = []
    list2 = []
    distances = []
    similarity_scores = []

    # Declare variables
    sum = 0
    similarity_sum = 0
    count = 0

    # Split the file into individual rows
    for line in f:
        row = line.split()
        # Create lists for each column
        list1.append(row[0])
        list2.append(row[1])

    # Sort the lists
    list1.sort()
    list2.sort()

    # Calculate distances between list items
    for i in range(0, len(list1)):
        distances.append(abs(int(list1[i])-int(list2[i])))

    # Sum distances between list items
    for i in range(0, len(distances)):
        sum = sum + distances[i]

    # Calculate similarity scores for each left list item
    for i in range(0, len(list1)):
        for j in range(0, len(list2)):
            if list1[i] == list2[j]:
                count = count + 1
        similarity_scores.append(int(list1[i]) * count)
        count = 0

    # Sum similarity scores
    for i in range(0, len(similarity_scores)):
        similarity_sum = similarity_sum + similarity_scores[i]

    # Print sum
    print("Sum of distances:", sum)

    # Print similarity_sum
    print("Sum of similarity scores:", similarity_sum)

    # Close file
    f.close()

# Provide an error message if file not found
except FileNotFoundError:
    print("File not found.")