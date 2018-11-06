# -*- coding: utf-8 -*-
# Write a program to calculate cubic root of float numbers using binary search
import math


def cubic_root(w=float(), e=float()):
    """ Calculate cubic root of float by binary search"""
    left = 0.0
    right = float(w)
    guesscount = 0
    tested = float(left + right) / 2.0
    while math.fabs(tested**3-w) >= e:
        if tested**3 < w:
            left = tested
        else:
            right = tested
        tested = (left + right) / 2.0
        guesscount += 1
    return tested, guesscount


def main(**kwargs):
    print("Enter a float for the number and a float for the quality to calculate the cubic root of the number.")
    value = float(input("[INPUT W]> "))
    quality = float(input("[INPUT EPSILON]> ").replace(",", "."))
    root, count = cubic_root(value, quality)
    print("Calculated a value of " + str(root) + ".")
    print("Took " + str(count) + " steps.")


if __name__ == "__main__":
    main()
