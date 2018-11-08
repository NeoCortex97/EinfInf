# -*- coding: utf-8 -*-
# Write a function which transforms decimal number to binary
from util_functions import *


def bin_to_dec(text=""):
    """ decodes binary number to decimal"""
    if test_alphabet(text, "10") and len(text) > 0:
        place = 0
        result = 0
        for c in reversed(text):
            result += int(c) * (2**place)
            place += 1
        return result
    return None


def find_place_count(number):
    """ Finds the number of places of a decimal number in binary"""
    exp = 0
    while 2 ** (exp + 1) < number:
        exp += 1
    return exp


def dec_to_bin(value):
    """ Encodes a decimal number to binary"""
    if test_alphabet(value, "0123456789") and len(value) > 0:
        decimal = int(value)
        if decimal == 0:
            return "0"
        else:
            nums = find_place_count(decimal)
            result = ""
            for pos in range(nums + 1):
                if decimal - (2 ** (nums - pos)) >= 0:
                    result += "1"
                    decimal = decimal - (2 ** (nums - pos))
                else:
                    result += "0"
            return result
    return None


def main(**kwargs):
    """ Main program to execute the functions"""
    print("Lets you encode or decode a number between binary and decimal representation.")
    command = ""
    last = ""
    while command.lower() != "quit":
        command = input("[COMMAND] quit/decode/ENCODE > ")
        if command.lower() in "encode":
            i = input("[INPUT](leave blank to use last value)>")
            if i != "":
                last = i
            print(str(last) + " in  binary is " + dec_to_bin(last))
        elif command.lower() in "decode":
            i = input("[INPUT](leave blank to use last value)>")
            if i != "":
                last = i
            print(str(last) + " in deimal is " + bin_to_dec(last))


if __name__ == "__main__":
    main()
