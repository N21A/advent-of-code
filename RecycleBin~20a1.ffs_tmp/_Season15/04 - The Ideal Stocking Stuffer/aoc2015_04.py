"""
aoc2015_04.py
----------------
Author: Nida Anis
Date: 23/12/2024
----------------
Description:
Solution to Advent of Code 2015 Day 4: The Ideal Stocking Stuffer
"""

# Import relevant modules
import hashlib

PUZZLE_INPUT = "bgvyzdsv"

# Initialise variables
hash_result = ""
count = 0

# While loop iterates until there are five leading zeroes
while hash_result[:5] != '00000':
    count = count + 1

    input_str = PUZZLE_INPUT + str(count)

    # Create an MD5 hash object
    md5_hash = hashlib.md5()

    # Update the hash object with the string
    md5_hash.update(input_str.encode('utf-8'))

    # Get the hash result
    hash_result = md5_hash.hexdigest()

# Print the hash result
print("The first hash result with five leading zeroes is:", hash_result)

# Print the count
print("The count equals:", count)

# Re-initialise variables
hash_result = ""
count = 0

# While loop iterates until there are siz leading zeroes
while hash_result[:6] != '000000':
    count = count + 1

    input_str = PUZZLE_INPUT + str(count)

    # Create an MD5 hash object
    md5_hash = hashlib.md5()

    # Update the has object with the string
    md5_hash.update(input_str.encode('utf-8'))

    # Get the hash result
    hash_result = md5_hash.hexdigest()

# Print the hash result
print("The first hash result with six leading zeroes is:", hash_result)

# Print the count
print("The count equals:", count)
