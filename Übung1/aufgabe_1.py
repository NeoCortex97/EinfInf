# -*- coding: utf-8 -*-
# Write a program to calculate faculty
# Input is integer > 0
# Output is faculty of input

# program breaks if you input negative number
from math import factorial as mfactorial


def ofactorial(num):
    """ Calculates the factorial of a positive integer number. returns integer"""
    result = 1
    for i in range(1, num + 1):
        result *= i
    return result


def main(**kwargs):
    print("This calculates the factorial of an integer.")
    to_compute = int(input("[EINGABE]> "))
    print("Own  Faculty: " + str(ofactorial(to_compute)))
    print("Math Faculty: " + str(mfactorial(to_compute)))


if __name__ == "__main__":
    main()
