# -*- coding: utf-8 -*-
# Write a program that checks for correctness of bracket expressions
# Part A: Write a Function that checks if an input contains only brackets and print result
#         This is implemented in check_for_invalid_characters
# Part B: Expand the program to check if the input is a valid bracket expression if condition A is met
#         This is implemented in check_for_matching_brackets

# Input: string
# Output: result of the checks
import sys
from util_functions import *


def check_for_matching_brackets(value):
    """ Checks if the bracket expression entered is valid by calculating the difference between opening and closing
    brackets."""
    level = 0
    for c in value:
        if c == "(":
            level += 1
        else:
            level -= 1
    if level == 0:
        print("The input is a valid bracket expression.")
    elif level > 0:
        print("Missing \")\" was detected!")
    else:
        print("Missing \"(\" was detected!")


def main(**kwargs):
    print("Enter a bracket expression to check if the brackets match")
    text = input("[EXPRESSION]> ")
    if test_alphabet(text, "()"):
        print("Input contains no invalid characters")
        check_for_matching_brackets(text)
    else:
        print("Input contains invalid characters!\nAborting!")


if __name__ == "__main__":
    main()
