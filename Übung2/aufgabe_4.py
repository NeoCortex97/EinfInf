# -*- coding: utf-8 -*-
# Write a function which transforms decimal number to binary


def checkChars(text="", allowed=""):
    result = True
    for c in text:
        if c not in allowed:
            result = False
    return result


def binToDec(text=""):
    if checkChars(text, "10") and len(text) > 0:
        place = 0
        result = 0
        for c in reversed(text):
            result += int(c) * (2**place)
            place += 1
        return result
    return None


def findPlaceCount(number):
    exp = 0
    while 2 ** (exp + 1) < number:
        exp += 1
    return exp


def decToBin(value):
    if checkChars(value, "0123456789") and len(value) > 0:
        decnum = int(value)
        if decnum == 0:
            return "0"
        else:
            nums = findPlaceCount(decnum)
            result = ""
            for pos in range(nums + 1):
                if decnum - (2 ** (nums - pos)) >= 0:
                    result += "1"
                    decnum = decnum - (2 ** (nums - pos))
                else:
                    result += "0"
            return result
    return None


def main():
    comand = ""
    last = ""
    while comand.lower() != "quit":
        comand = input("[COMAND] quit/decode/ENCODE > ")
        if comand.lower() in "encode":
            i = input("[INPUT](leave blank to use last value)>")
            if i != "":
                last = i
            print(str(last) + " in  binary is " + decToBin(last))
        elif comand.lower() in "decode":
            i = input("[INPUT](leave blank to use last value)>")
            if i != "":
                last = i
            print(str(last) + " in deimal is " + binToDec(last))


if __name__ == "__main__":
    main()