# -*- coding: utf-8 -*-
# Stefan Schmelz Mat.Nr.: 35221810
# Ingo Kehres    Mat.Nr.: 33318235
# Siamak Najafi  Mat-Nr.: 33397081


def possible_moves(pos=tuple(), size=int()):
    moves = [(2,1), (1,2), (-2, 1), (-1, 2), (2, -1), (1, -2), (-2, -1), (-1, -2)]
    results = list()
    for m in moves:
        if 0 <= pos[0] + m[0] < size and 0 <= pos[1] + m[1] < size:
            # print("appending ", pos + m)
            results.append((pos[0] + m[0], pos[1] + m[1]))
    return results


def min_moves(brett, position, steps=1):
    for m in possible_moves(position, len(brett)):
        if brett[m[0]][m[1]] < 0 or brett[m[0]][m[1]] > steps:
            brett[m[0]][m[1]] = steps
            min_moves(brett, m, steps + 1)



def main(**kwargs):
    print("Startwerte:")
    boardSize = int(input("[BOARD GÖSSE]> "))
    startPos = int(input("[STARTPOSITION X]> ")), int(input("[STARTPOSITION Y]> "))
    brett = [[-1 for j in range(boardSize)] for i in range(boardSize)]
    brett[startPos[0]][startPos[1]] = 0
    print("test ob spielfeld okay:")
    print("y ->")
    print("x\n|\nv")
    for item in brett:
        print(item)
    print("Possible moves okay?")
    print(possible_moves(startPos, boardSize))
    print("calcaulating minimum number of moves...")
    min_moves(brett, startPos)
    for e in brett:
        print(e)



if __name__ == "__main__":
    main()