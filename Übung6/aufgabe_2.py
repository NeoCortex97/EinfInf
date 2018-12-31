# -*- coding: utf-8 -*-
# Stefan Schmelz Mat.Nr.: 35221810
# Ingo Kehres    Mat.Nr.: 33318235
# Siamak Najafi  Mat-Nr.: 33397081


def lies_ein():
    with open("dictionary.txt") as file:
        return [line.strip("\n") for line in file]


def buck_1(liste):
    return {i: len(i) for i in liste}


def fib(n):
    if n in [0, 1]:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def buch_2():
    return {n: fib(n) for n in range(30)}


def fibonaccilaenge(wort=str(), buch1=dict(), buch2=dict()):
    if not wort in buch1.keys():
        return None
    else:
        if not buch1[wort] in buch2:
            return None
        else:
            return buch2[buch1[wort]]


def main(**kwargs):
    b1 = buck_1(lies_ein())
    b2 = buch_2()
    print(fibonaccilaenge(input("[WORT]> "), b1, b2))


if __name__ == "__main__":
    main()
