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


def main():
    value = float(input("[INPUT W]> "))
    quality = float(input("[INPUT EPSILON]> "))
    print(cubic_root(value, quality))


if __name__ == "__main__":
    main()
