# -*- coding: utf-8 -*-


def test_alphabet(text="", alphabet=""):
    for c in text:
        if c not in alphabet:
            return False
    return True
