# Write a program that draws a rectangle
# Inputs A(width); B(height)
# -*- coding: utf-8 -*-
import sys



def draw_horizontal_side(length):
    """ Prints a series of - with specified length. returns nothing"""
    sys.stdout.write(" ")
    for _a in range(int(length)):
        sys.stdout.write("-")
    sys.stdout.write("\n")


def draw_slice(length):
    """ Prints a slice of the sides. returns nothing"""
    sys.stdout.write("|")
    for _a in range(int(length)):
        sys.stdout.write(" ")
    sys.stdout.write("|\n")


def rect(a, b):
    """draws a rectangel with width of a and height of b. returns nothing"""
    draw_horizontal_side(a)
    for _b in range(int(b)):
        draw_slice(a)
    draw_horizontal_side(a)


if __name__ == "__main__":
    rect(input("[WIDTH]> "), input("[HEIGHT]> "))
