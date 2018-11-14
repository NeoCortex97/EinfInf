# -*- coding: utf-8 -*-
# Stefan Schmelz Mat.Nr.: 35221810
# Ingo Kehres    Mat.Nr.: 
# Siamak Najafi  Mat-Nr.: 33397081


def sanatize(text=""):
    return text.strip(" \"<>").lower()


def palindrome(text=""):
    if len(text) == 2:
        if text[0] == text[1]:
            return True
    elif len(text) == 3:
        if text[0] == text[-1]:
            return True
    elif len(text) >= 4:
        if text[0] == text[-1]:
            return palindrome(text[1:-1])
    return False


def main(**kwargs):
    print("Please input a palindrome!")
    text = input("[TEXT]> ")
    if palindrome(text):
        print("Yep")
    else:
        print("Nope")


if __name__ == "__main__":
    main()
