# -*- coding: utf-8 -*-
# Write a program that checks if a word is contained in a dictionary
# Part A: write a function find_pos which accepts a string and a character and returns the position of the character in
#         the string if it exists and if it doesn't exist it returns -1
# Part B: write a function that converts the dictionary to a text file which only contains the words
# Part C: write a program that accepts a word and outputs the line number of the word in the new dictionary if it is
#         contained in the dictionary.
import sys


def find_pos(string, char):
    """ returns the index of a char in a string if it is contained. else it returns -1"""
    pos = 0
    for c in string:
        if c == char:
            return pos
        pos += 1
    return -1


def convert_dictionary(old_dic, new_dic):
    """ Converts a dictionary file to a collection of words"""
    # The encoding is necessary because the script is encoded in utf-8 and python assumes the opened files are encoded
    # in utf-8 too
    infile = open(old_dic, "r", encoding="iso8859-15")
    outfile = open(new_dic, "w", encoding="iso8859-15")
    pc = 0
    current_line = infile.readline()
    # read every line in the file and discard comments and empty lines
    while current_line != "":
        pc += 1
        if pc % 10 == 0:
            sys.stdout.write(".")
        if ("# " not in current_line) and (current_line != "\n"):
            if find_pos(current_line, "#") == -1:
                if "	\n" != current_line:
                    outfile.write(current_line[0:find_pos(current_line, "/")] + "\n")
        current_line = infile.readline()
    infile.close()
    outfile.close()


def find_in_dic(word):
    """ returns the index of a word in the dictionary if it is contained. else it returns -1"""
    pos = 0
    try:
        infile = open("dictionary.txt", "r", encoding="iso8859-15")
    except IOError:
        print("PLEASE WAIT! THE DICTIONARY IS CONVERTED!")
        convert_dictionary("de_DE_frami.dic", "dictionary.txt")
        infile = open("dictionary.txt", "r", encoding="iso8859-15")
    line = infile.readline()
    while line != "":
        if line == word + "\n":
            return pos
        pos += 1
        line = infile.readline()
    return -1


def main():
    """ Main program to search"""
    abort = False
    while not abort:
        word = input("[WORT]> ")
        position = find_in_dic(word)
        if position != -1:
            print("YOUR WORD WAS FOUND AT INDEX: " + str(position))
        else:
            print("IM SORRY; BUT  COULD NOT FIND YOUR WORD IN THE CURRENT DICTIONARY....")
        if input("[CONTINUE](yes/NO)> ").lower() in "no":
            abort = True


if __name__ == "__main__":
    main()
