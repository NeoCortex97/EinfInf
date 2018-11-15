# -*- coding: utf-8 -*-
# Stefan Schmelz Mat.Nr.: 35221810
# Ingo Kehres    Mat.Nr.: 
# Siamak Najafi  Mat-Nr.: 33397081

# Interpretiert einen string der form:  a +   b +   c +   d +   e + ...
# in folgender weise:                 ( a + ( b + ( c + ( d + ( e + ....) ) ) ) )


def parse(text=""):
    try:
        return int(text)
    except ValueError:
        # print("PENG")
        num = ""
        i = 0
        while text[i].isnumeric():
            num += text[i]
            i += 1
        if text[i] == "+":
            n2 = parse(text[i + 1:])
            if n2 >= 0:
                return int(num) + n2
    return -1


def sanatize(text=""):
    return text.strip(" ")


def main(**kwargs):
    print("Enter a addition term!")
    print("Die Summe ist " + str(parse(sanatize(input("[TERM]> ")))))


if __name__ == "__main__":
    main()
