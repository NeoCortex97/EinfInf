# -*- coding: utf-8 -*-
from util_functions import *


def find_closing(text):
    index = 0
    depth = 0
    if len(text) > 1:
        for c in text:
            if c == "(":
                depth += 1
                #print("increasing depth")
            else:
                depth -= 1
                #print("decreasing depth")
            index += 1
            #print("Index: {0:^5} \nChar: {1:^5}\nDepth: {2:^5}".format(index, c, depth))
            if depth == 0:
                break
        #print("Found match at {:5}".format(index))
        return index
    else:
        #print("String is to short to contain a matching pair of brackets!")
        return -1


def test_pairs(text=""):
    if text == "()":
        #print("Found empty word.")
        return True
    elif len(text) > 0:
        mindex = 0
        if text[0] == "(":
            #print("Found opening! Seeking closing . . .")
            mindex = find_closing(text)
            if mindex > 0:
                #print("{0:<20} {1:<30}\n{2:<20} {3:<30}".format("First part:", text[1:mindex -1], "Second part:", text[mindex:]))
                if test_pairs(text[1:mindex - 1]) and test_pairs(text[mindex:]):
                    #print("first and second half are okay")
                    return True
                else:
                    #print("one of the halfes does not match")
                    return False
            else:
                return False
    else:
        return True

def main(**kwargs):
    ausdruck = input("[EXPRESSION]> ")
    if test_alphabet(ausdruck, "()"):
        if test_pairs(ausdruck):
            print("Ausdruck ist okay.")
        else:
            print("Ausdruck ist falsch")
    else:
        print("Ausdruck enthält ungültige Zeichen.")

if __name__ == "__main__":
    main()