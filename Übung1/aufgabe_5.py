# -*- coding: utf-8 -*-
# Write a program that processes a sum from a string
import sys


def sanatize(value):
    result = value.replace(" ", "")
    allowed = "0123456789+"
    for c in result:
        if c not in allowed:
            print("unknown characters detected!\nAborting!")
            sys.exit(-1)
    nums = result.split("+")
    for n in nums:
        if len(n) != 1:
            print("Bad number length!\nAborting!")
            sys.exit(-1)
    return nums


def add_list(vals):
    result = 0
    for num in vals:
        result += int(num)
    return result


def main():
    numbers = sanatize(input("[TERM]> "))
    print("THE SUM OF THE TERM IS: " + str(add_list(numbers)))


if __name__ == "__main__":
    main()
