# -*- coding: utf-8 -*-
# Write a program that reads a string, converts it to lowercase and replaces all vowels with a specified one
# input: string
# output: the processed string


def proc_string(value, rep):
    """ Converts a string to lowercase and replaces al vowels with a specified one. returns nothing"""
    lower = value.lower()
    vowels = "aeiou"
    replaced = lower
    for v in vowels:
        replaced = replaced.replace(v, rep)
    print("ORIGINAL:  " + value)
    print("LOWERCASE: " + lower)
    print("REPLACED:  " + replaced)


def main(**kwargs):
    print("Enter a string and a vowel and replace all vowels with the entered one.")
    proc_string(input("[STRING]> "), input("[VOWEL]> "))


if __name__ == "__main__":
    main()
