# -*- coding: utf-8 -*-
# Write a program that verifies that a input consists only of allowed characters
# and count the number of occurences
# input: string
# allowed chars: a b c

def print_results(a, b, c):
    """ Prints the results as a table. returns nothing"""
    print("╒═════╤═════╕")
    print("│count│char│")
    print("╞═════╪═════╡")
    print("│{:^5}│".format(a) + " a  │")
    print("│{:^5}│".format(b) + " b  │")
    print("│{:^5}│".format(c) + " c  │")
    print("╘═════╧═════╛")


def verify_and_count(value):
    """ Veriefies, that a string contains only as, bs and cs, while counting them. return nothing"""
    count_a = 0
    count_b = 0
    count_c = 0
    for c in value:
        if c == "a":
            count_a += 1
        elif c == "b":
            count_b += 1
        elif c == "c":
            count_c += 1
        else:
            print("How dare you enter invalid characters :-)")
            break
    print_results(count_a, count_b, count_c)


if __name__ == "__main__":
    verify_and_count(input("[STRING]> "))
