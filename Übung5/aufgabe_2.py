# -*- coding: utf-8 -*-
# Stefan Schmelz Mat.Nr.: 35221810
# Ingo Kehres    Mat.Nr.: 33318235
# Siamak Najafi  Mat-Nr.: 33397081
import random


def init(x=int):
    return tuple(random.randint(1, x + 1) for i in range(7))


def mkKey(data=list()):
    result = ""
    for item in data:
        result += str(item) + " "
    return result[:-1]


def initCache(length=int()):
    result = dict()
    for i in range(length):
        l = list()
        for j in range(length):
            if i == j:
                l.append(1)
            else:
                l.append(0)
        result[mkKey(l)] = -1
    return result


def strategie(field=tuple(), cache=dict()):
    key = mkKey(field)
    if key in cache:
        return cache[key]
    elif getNonEmptyStackCount(field) > 0:
        strs = ["{0:04b}".format(x) for x in field]
        lastSum = 0
        for i in strs:
            lastSum += int(i[-1])
        pos = field.index(max(field))
        if lastSum % 2 != 0:
            cache[key] = pos, 1
            return pos, 1
        else:
            cache[key] = pos, 2


def main(**kwargs):
    playfield = init(7)
    print("Startzustand Spielfeld ", playfield)
    cache = initCache(7)
    print("Startzustand Cache ", cache)
    strategie(playfield, cache)



if __name__ == "__main__":
    main()