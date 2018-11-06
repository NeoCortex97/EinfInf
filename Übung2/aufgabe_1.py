# -*- coding: utf-8 -*-
# Write a program that encodes a ascii string with cesar cypher
# Part A: write a function, that returns True if the passed string is ascii characters only
# Part B: write a function called cesar which accepts a ascii string and a int to encodes it with cesar cypher
# Part c: write a function called un_cesar which accepts a ascii string and a int to decode it with cesar cypher
# Part D: use the functions to write a program which asks if a string should be encoded or decoded and
#         outputs the processed string

# Notice: der parameter **kwargs ist im pattern für python Dateien bei mir verankert und hauptsächlich vorhanden um
#         gegebenenfalls auch mit daten aus einem anderen Verzeichnis testen zu können.


def is_ascii(value):
    """ Check if a string contains only ascii chars"""
    for c in value:
        if ord(c) > 127:
            return False
    return True


def cesar(cypher, offset):
    """ Encode a text with cesar cypher"""
    result = ""
    for c in cypher:
        result += chr((ord(c) + offset) % 128)
    return result


def un_cesar(cypher, offset):
    """ Decode a cesar cyphered text to plain text"""
    result = ""
    for c in cypher:
        result += chr(abs((ord(c) - offset) % 128))
    return result


def main(**kwargs):
    """ Main program to apply encode and decode functions"""
    print("Lets you encode or decode a string with cesar cypher.")
    task = 0
    while task == 0:
        i = input("[ENCODE OR DECODE]> ").lower()
        if i == "encode":
            task = 1
        elif i == "decode":
            task = 2
    text = input("[CYPHER TEXT]> ")
    offset = int(input("[OFFSET]> "))
    if task == 1:
        print(cesar(text, offset))
    else:
        print(un_cesar(text, offset))


if __name__ == "__main__":
    main()
