"""
aoc2024_07_2.py
----------------
Author: Nida Anis
Date: 28/12/2024
----------------
Description:
- Advent of Code 2024 Day 7: Bridge Repair
- Solution to Part 2 (Part 1 in aoc2024_07_1.py)
"""

from aoc2024_07_1 import create_equation_dict

# Import relevant modules
from itertools import product

def evaluate_expression_with_concatenation(numbers, operators):
    """
    Evaluates the expression left-to-right given a list of numbers and operators.
    Valid operators: +, *, ||
    """
    result = numbers[0]
    for i, op in enumerate(operators):
        if op == '+':
            result += numbers[i+1]
        elif op == '*':
            result *= numbers[i+1]
        elif op == '||':
            result = int(str(result) + str(numbers[i+1]))
    
    return result

def check_valid_equation_with_concatenation(target, numbers):
    """
    Checks if the given sequence of numbers can produce the target using +, *, and || operators.
    Valid operators: +, *, ||
    -> If valid, returns True.
    -> If not valid, returns False.
    """
    if len(numbers) == 1: # Single number case
        return target == numbers[0]
    
    # Generate all possible combinations of operators
    operator_combinations = product(['+', '*', '||'], repeat=len(numbers) - 1)

    # Checkl all combinations against the target
    for operators in operator_combinations:
        if evaluate_expression_with_concatenation(numbers, operators) == target:
            return True
    
    return False

def main():
    equation_dict = create_equation_dict()
    total_calibration_result = 0
    valid_expressions_count = 0

    for target, numbers in equation_dict.items():
        print("Evaluating target:", target)
        if check_valid_equation_with_concatenation(target, numbers):
            valid_expressions_count += 1
            total_calibration_result += target
            print(f"    -> Valid expression found! (Total: {valid_expressions_count})")

    print("Total calibration result:", total_calibration_result)
    
if __name__ == "__main__":
    main()