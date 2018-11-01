# Write a program that draws a rectangle
# Inputs A(width); B(height)
# -*- coding: utf-8 -*-
import sys



def draw_horizontal_side(length):
    sys.stdout.write(" ")
    for _a in range(int(length)):
        sys.stdout.write("-")
    sys.stdout.write("\n")


def draw_slice(length):
    sys.stdout.write("|")
    for _a in range(int(length)):
        sys.stdout.write(" ")
    sys.stdout.write("|\n")


def rect(a, b):
    draw_horizontal_side(a)
    for _b in range(int(b)):
        draw_slice(a)
    draw_horizontal_side(a)


if __name__ == "__main__":
    rect(input("[WIDTH]> "), input("[HEIGHT]> "))
