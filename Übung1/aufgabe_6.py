# -*- coding: utf-8 -*-
# Write a program that checks for correctness of bracket expressions
# Part A: Write a Function that checks if an input contains only brackets and print result
#         This is implemented in check_for_invalid_characters
# Part B: Expand the program to check if the input is a valid bracket expression if condition A is met
#         This is implemented in check_for_matching_brackets

# Input: string
# Output: result of the checks
import sys


def check_for_invalid_characters(value, allowed):
    """ Checks if a string contains any unwanted parameters. returns nothing, but stops the program if it finds any"""
    for c in value:
        if c not in allowed:
            print("Invalid input character!\nAborting!")
            sys.exit(-1)
    print("Input contains no invalid characters.")


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


def main():
    text = input("[EXPRESSION]> ")
    check_for_invalid_characters(text, "()")
    check_for_matching_brackets(text)


if __name__ == "__main__":
    main()
