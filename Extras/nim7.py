# -*- coding: utf-8 -*-
# Stefan Schmelz Mat.Nr.: 35221810
# Ingo Kehres    Mat.Nr.: 33318235
# Siamak Najafi  Mat-Nr.: 33397081
import random


def main(**kwargs):
    max = 5
    count = 7
    field = [random.randint(1, max + 1) for i in  range(count)]
    turn = 0
    while sum(field) > 0:
        print("Spielfeld: ", field)
        if turn == 0:
            print("player 1 ist dran:")
        else:
            print("player 2 ist dran:")
        stack = int(input("[STACK]> "))
        amount = int(input("[AMOUNT]> "))
        if 0 < field[stack - 1] >= amount:
            field[stack - 1] -= amount
            turn = (turn + 1) % 2
        else:
            print("Nope")
    print("spieler {} hat gewonnen".format(turn + 1))


if __name__ == "__main__":
    main()