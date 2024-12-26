"""
aoc2024_05.py
----------------
Author: Nida Anis
Date: 24/12/2024
----------------
Description:
Solution to Advent of Code 2024 Day 5: Print Queue
"""

# Import relevant modules
import re
import numpy as np

def get_page_info():
    """
    Gets page information from the input.txt file.
    """

    with open("input.txt", "r") as f:

        # Initialise arrays
        page_ordering_rules = []
        pages_to_produce = []

        # Initialise variables
        after_break = False

        # Read lines into correct arrays
        for line in f:
            if line.strip() == "":
                after_break = True

            if after_break == False:
                page_ordering_rules.append(line.strip())
            elif after_break == True and line.strip() != "":
                pages_to_produce.append(line.strip())

        return page_ordering_rules, pages_to_produce
    
def create_ordering_dict(page_ordering_rules):
    """
    Creates a dictionary containing page ordering information.
    """

    # Initialise dictionaries
    ordering_dict = {}

    for line in page_ordering_rules:
        # Extract page and term
        page = int(re.search(r'^\d+', line).group())
        term = int(re.search(r'(?<=\|)\d+', line).group())

        # If the page number isn't in the dictionary, add a blank entry
        if page not in ordering_dict:
            ordering_dict[page] = []

        # Append the term to the corresponding page entry
        ordering_dict[page].append(term)

    return ordering_dict

def check_page_updates(pages_to_produce, ordering_dict):
    """
    Checks page updates to see if they're valid.
    Adds valid page updates to an array, valid_updates.
    """

    # Initialise arrays
    valid_updates = []
    invalid_updates = []
    conflict_checks = []

    # Initialise variables
    conflict = False

    # Convert the pages to produce list into a two-dimensional array
    page_updates = [list(map(int, line.split(','))) for line in pages_to_produce]

    for update in page_updates:
        conflict_checks = []
        for i in range(1, len(update)):
            current_item = update[i]
            previous_items = update[:i]

            # Check if the current item is in ordering_dict
            if current_item in ordering_dict:
                # Get the dictionary entry for the current item
                current_values = ordering_dict[current_item]

                # Check if any previous conflicts appear in the previous items
                conflict = any(item in current_values for item in previous_items)
                conflict_checks.append(conflict)
            
            if i == len(update) - 1 and all(check == False for check in conflict_checks):
                valid_updates.append(update)
            
            else:
                if i == len(update) - 1 and not all(check == False for check in conflict_checks):
                    invalid_updates.append(update)

    return valid_updates, invalid_updates

def count_middle_pages(valid_updates):
    """
    Adds up the middle page numbers of valid updates.
    """
    # Initialise variables
    middle_page_sum = 0

    for update in valid_updates:
        middle_index = len(update) // 2
        middle_page = update[middle_index]
        middle_page_sum += middle_page
    
    return middle_page_sum

def reorder_invalid_updates(invalid_updates, ordering_dict):
    """
    Reorders invalid updates.
    Adds reordered updates to the reorded_updates array.
    """

    # Initialise arrays
    reordered_updates = []

    # Initialise variables
    conflicts_resolved = False
    
    for update in invalid_updates:
        # Make a copy of the current update
        reordered_update = update[:]

        for i in range(len(reordered_update)):
            # Start from the current index and work backwards
            for j in range(i, 0, -1):
                current_item = reordered_update[j]
                previous_item = reordered_update[j-1]

                # Check if the current item is in ordering_dict
                if current_item in ordering_dict:
                    # Get the dictionary entry for the current item
                    current_values = ordering_dict[current_item]

                    # Detect and resolve conflicts
                    if previous_item in current_values:
                        # Swap conflicting items
                        reordered_update[j], reordered_update[j - 1] = (
                            reordered_update[j - 1],
                            reordered_update[j]
                        ) 
                    
                    # If there isn't a conflict, move to next item
                    else:
                        break
        
        if reordered_update not in reordered_updates:
            reordered_updates.append(reordered_update)
        
    return reordered_updates

def main():
    """
    Main program.
    Contains solutions to:
    - Day 5: Part 1
    - Day 5: Part 2
    """

    # Day 5: Part 1
    print("PART 1:")
    page_ordering_rules, pages_to_produce = get_page_info()
    ordering_dict = create_ordering_dict(page_ordering_rules)
    valid_updates = check_page_updates(pages_to_produce, ordering_dict)[0]
    print("Number of valid updates:", len(valid_updates))
    middle_page_sum = count_middle_pages(valid_updates)
    print("Sum of middle pages:", middle_page_sum)

    # Day 5: Part 2
    print("PART 2:")
    invalid_updates = check_page_updates(pages_to_produce, ordering_dict)[1]
    print("Number of invalid updates:", len(invalid_updates))
    reordered_updates = reorder_invalid_updates(invalid_updates, ordering_dict)
    print("Number of reordered updates:", len(reordered_updates))
    middle_page_sum = count_middle_pages(reordered_updates)
    print("Sum of reordered middle pages:", middle_page_sum)

if __name__ == "__main__":
    main()