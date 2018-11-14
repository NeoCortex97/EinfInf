# -*- coding: utf-8 -*-
# Stefan Schmelz Mat.Nr.: 35221810
# Ingo Kehres    Mat.Nr.: 
# Siamak Najafi  Mat-Nr.: 33397081


def fib(n=0):
    if n < 2:
        return n
    return fib(n - 2) + fib(n - 1)


def main(**kwargs):
    n = input("[MONTHS]> ")
    print("Nach {0:>3} Monaten gibt es {1:>4} Hasen.".format(n, fib(int(n))))


if __name__ == "__main__":
    main()
