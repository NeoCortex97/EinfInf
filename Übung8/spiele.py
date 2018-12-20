# -*- coding: utf-8 -*-
# Stefan Schmelz Mat.Nr.: 35221810
# Ingo Kehres    Mat.Nr.: 33318235
# Siamak Najafi  Mat-Nr.: 33397081


def kodh(count):
    if count == 1:
        return 0
    else:
        result = 0
        for i in range(count - 1):
            result += 1
        return result


def si(count):
    if count == 2:
        return 1
    else:
        return 2 * si(count / 2)


def rr(count):
    return (2 * count) - 1

def km(count):
    if count == 1:
        return 0
    elif count == 2:
        return 1
    else:
        return 1 + 2 * km(count - 1)


def times(methode="", mins=int()):
    h = mins / 60
    d = h / 24
    w = d / 7
    m = w / 4
    j = m / 12
    print("{}: {} Minuten | {} Stunden | {} Tage | {} Wochen | {} Monate | {} Jahre".format(methode, mins, h, d, w, m, j))


def main(**kwargs):
    c = 32
    times("King Of The Hill", kodh(c))
    times("Single Elimination", si(c))
    times("Round Robin", rr(c))
    times("Kassler Methode", km(c))


if __name__ == "__main__":
    main()
