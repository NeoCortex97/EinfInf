# -*- coding: utf-8 -*-
# Stefan Schmelz Mat.Nr.: 35221810
# Ingo Kehres    Mat.Nr.: 33318235
# Siamak Najafi  Mat-Nr.: 33397081
import itertools
import math


def main(**kwargs):
    for n in itertools.count(1):
        if n <= n:
            print("i)   {}".format(n))
            break
    for n in itertools.count(1):
        if 100 * n ** 2 <= n**3:
            print("ii)  {}".format(n))
            break
    for n in  itertools.count(1):
        if 10 * n <= (n ** 2) - 10 * n:
            print("iv)  {}".format(n))
            break
    for n in itertools.count(1):
        if n * math.log2(n) <= 0.05 * n ** 2 - 4 * n:
            print("v)   {}".format(n))
            break
    for n in  itertools.count(1):
        if 1000 * (n ** 2) <= 0.25 * 2 ** n:
            print("vi)  {}".format(n))
            break


if __name__ == "__main__":
    main()