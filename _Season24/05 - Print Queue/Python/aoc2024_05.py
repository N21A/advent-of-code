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
            elif after_break == True:
                pages_to_produce.append(line.strip())

        return page_ordering_rules, pages_to_produce
    
def create_ordering_dict(page_ordering_rules):
    """
    Creates a dictionary containing page ordering information.
    """

    # Initialise dictionaries
    ordering_dict = {}

    for line in page_ordering_rules:
        page = int(re.search(r'^\d+', line).group())

    return ordering_dict
    
def main():
    page_ordering_rules, pages_to_produce = get_page_info()
    create_ordering_dict(page_ordering_rules)

if __name__ == "__main__":
    main()