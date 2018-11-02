# -*- coding: utf-8 -*-
# Write a program that checks if a word is contained in a dictionary
# Part A: write a function find_pos which accepts a string and a character and returns the position of the character in
#         the string if it exists and if it doesn't exist it returns -1
# Part B: write a function that converts the dictionary to a text file which only contains the words
# Part C: write a program that accepts a word and outputs the line number of the word in the new dictionary if it is
#         contained in the dictionary.
import sys


def find_pos(string, char):
    pos = 0
    for c in string:
        if c == char:
            return pos
        pos += 1
    return -1


def convert_dictionary(old_dic, new_dic):
    infile = open(old_dic, "r")
    outfile = open(new_dic, "w")
    pc = 0
    current_line = infile.readline()
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
    pos = 0
    infile = open("dictionary.txt", "r")
    line = infile.readline()
    while line != "":
        if line == word + "\n":
            return pos
        pos += 1
        line = infile.readline()
    return -1


def main():
    word = input("[WORT]> ")
    position = find_in_dic(word)
    if position != -1:
        print("YOUR WORD WAS FOUND AT INDEX: " + str(position))
    else:
        print("IM SORRY; BUT  COULD NOT FIND YOUR WORD IN THE CURRENT DICTIONARY....")

if __name__ == "__main__":
    #convert_dictionary("de_DE_frami.dic", "dictionary.txt")
    main()