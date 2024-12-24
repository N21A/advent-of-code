"""
aoc2016_05.py
----------------
Author: Nida Anis
Date: 23/12/2024
----------------
Description:
Solution to Advent of Code 2016 Day 5: How About a Nice Game of Chess?
"""

# Import relevant modules
import hashlib

PUZZLE_INPUT = "ojvtpuvg"

# Initialise variables
hash_result = ""
password = ""
pos_count = 0
char_count = 0

# While loop iterates until the password is eight characters long
while char_count != 8:
    pos_count += 1

    input_str = PUZZLE_INPUT + str(pos_count)

    # Create an MD5 hash object
    md5_hash = hashlib.md5()

    # Update the hash object with the string
    md5_hash.update(input_str.encode('utf-8'))

    # Get the hash result
    hash_result = md5_hash.hexdigest()

    # If an interesting hash is found:
    # - Add the character to the password
    # - Increment char_count by 1
    if hash_result[:5] == '00000':
        password = password + hash_result[5]
        char_count = char_count + 1

print("The first password is:", password)

# Re-initialise variables
hash_result = ""
password = ""
pos_count = 0
char_count = 0
is_valid = False

# Initialise arrays
positions = [0, 1, 2, 3, 4, 5, 6, 7]
password_arr = ["","","","","","","",""]

# While loop iterates until a valid password has been found
while is_valid != True:
    pos_count += 1

    input_str = PUZZLE_INPUT + str(pos_count)

    # Create an MD5 hash object
    md5_hash = hashlib.md5()
    
    # Update the hash object with the string
    md5_hash.update(input_str.encode('utf-8'))

    # Get the hash result
    hash_result = md5_hash.hexdigest()

    if hash_result[:5] == '00000':
        # Check if hash_result[5] is a valid position
        if hash_result[5].isdigit() and int(hash_result[5]) in positions:
            # Update the password array
            position = int(hash_result[5])
            password_arr[position] = hash_result[6]

            # Remove the position from the positions array
            positions.remove(position)
    
    if positions == []:
        for char in password_arr:
            password = password + char
        
    if len(password) == 8:
        is_valid = True

print("The second password is:", password)