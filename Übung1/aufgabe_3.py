# -*- coding: utf-8 -*-
# Write a program that verifies that a input consists only of allowed characters
# and count the number of occurences
# input: string
# allowed chars: a b c d

def print_results(a, b, c, d):
    """ Prints the results as a table. returns nothing"""
    print("╒" + ("═" * 10) + "╤" + ("═" * 10) + "╕")
    print("│{:^10}│".format("count") + "{:^10}│".format("char"))
    print("╞" + ("═" * 10) + "╪" + ("═" * 10) + "╡")
    print("│{:^10}│".format(a) + "{:^10}│".format("a"))
    print("│{:^10}│".format(b) + "{:^10}│".format("b"))
    print("│{:^10}│".format(c) + "{:^10}│".format("c"))
    print("│{:^10}│".format(d) + "{:^10}│".format("d"))
    print("╘" + ("═" * 10) + "╧" + ("═" * 10) + "╛")


def verify_and_count(value):
    """ Veriefies, that a string contains only as, bs, cs and ds, while counting them. return nothing"""
    count_a = 0
    count_b = 0
    count_c = 0
    count_d = 0
    for c in value:
        if c == "a":
            count_a += 1
        elif c == "b":
            count_b += 1
        elif c == "c":
            count_c += 1
        elif d == "d":
            count_d += 1
        else:
            print("How dare you enter invalid characters :-)")
            break
    print_results(count_a, count_b, count_c, count_d)


if __name__ == "__main__":
    verify_and_count(input("[STRING]> "))
