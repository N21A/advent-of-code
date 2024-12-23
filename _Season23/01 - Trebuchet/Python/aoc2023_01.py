# Advent of Code 2023 - Day 1: Trebuchet

# Define a list of 'numbers'
numbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']

# Declare lists
list1 = [] # List of original strings
list2 = [] # List of digit-only strings
list3 = [] # List of calibration values

# Declare variables
k = ""
l = ""
sum = 0

# Implement error handling
try:
    # Open input.txt
    f = open("input.txt", "r")

    # Read all lines into list1
    for line in f:
        list1.append(line.strip())

    # For each line in the file:
    for i in range(0, len(list1)):

        # For each character in the line:
        for j in range(0, len(list1[i])):
            # If the character is a digit, add to 'k'
            if list1[i][j].isdigit():
                k = k + list1[i][j]

        # Append the value of 'k' for each line to list2
        list2.append(k)
        # Clear 'k'
        k = ""
    
    # Find calibration values
    for i in range(0, len(list2)):
        # For strings of digits > 1 characters
        if len(list2[i]) > 1:
            l = list2[i][0] + list2[i][-1]
        # For strings of digits = 1 character
        else:
            l = list2[i] + list2[i]
        # Append to list3
        list3.append(l)
    
    # Sum calibration values
    for i in range(0, len(list3)):
        sum = sum + int(list3[i])

    # Print sum
    print("Sum of calibration values: ", sum)

    # Close file
    f.close()

except FileNotFoundError:
    print("File not found.")