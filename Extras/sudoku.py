# -*- coding: utf-8 -*-

# box character: ╔ ═ ║ ╗ ╚ ╝ ╟ ╠ ╢ ╣ ╤ ╦ ╧ ╩ ╬ │ ─ ┼ ╫ ╪

class Sudoku:
    def __init__(self, prefilled=list()):
        self.field = [[[x for x in range(1, 10)] for y in range(9)] for z in range(9)]
        if len(prefilled) > 0:
            for p in prefilled:
                self.field[p[0]][p[1]] = p[2]

    def printRow(self, index=int()):
        val = lambda i, j: "   " if isinstance(self.field[i][j], list) else self.field[i][j]
        print("║{:^3}│{:^3}│{:^3}║{:^3}│{:^3}│{:^3}║{:^3}│{:^3}│{:^3}║".format(val(index, 0), val(index, 1), val(index, 2),
                                                                               val(index, 3), val(index, 4), val(index, 5),
                                                                               val(index, 6), val(index, 7), val(index, 8)))

    def printGrid(self):
        print("╔═══╤═══╤═══╦═══╤═══╤═══╦═══╤═══╤═══╗")
        self.printRow(0)
        for n in range(1, 9):
            print("╟───┼───┼───╫───┼───┼───╫───┼───┼───╢")
            self.printRow(n)
        print("╚═══╧═══╧═══╩═══╧═══╧═══╩═══╧═══╧═══╝")

    def reduceRow(self, index=int()):
        uniques = list()
        for p in range(9):
            if isinstance(self.field[index][p], int):
                uniques.append(self.field[index][p])
        count = 0
        for p in range(9):
            if isinstance(self.field[index][p], list):
                for u in uniques:
                    if u in self.field[index][p]:
                        self.field[index][p].remove(u)
                        count += 1
        # print("removed {} possible values.".format(count))
        return count

    def reduceCol(self, col=int()):
        uniques = list()
        for p in range(9):
            if isinstance(self.field[p][col], int):
                uniques.append(self.field[p][col])
        count = 0
        for p in range(9):
            if isinstance(self.field[p][col], list):
                for u in uniques:
                    if u in self.field[p][col]:
                        self.field[p][col].remove(u)
                        count += 1
        # print("removed {} possible values.".format(count))
        return count

    def reduceCell(self, col=int(), row=int()):
        cellIndexes = [((col * 3) + x, (row * 3) + y) for x in range(3) for y in range(3)]
        uniques = list()
        for c in cellIndexes:
            if isinstance(self.field[c[0]][c[1]], int):
                uniques.append(self.field[c[0]][c[1]])

        count = 0
        for c in cellIndexes:
            if isinstance(self.field[c[0]][c[1]], list):
                for u in uniques:
                    if u in self.field[c[0]][c[1]]:
                        self.field[c[0]][c[1]].remove(u)
                        count += 1
        return count

    def reduceBoard(self):
        count = 0
        for i in range(9):
            count += self.reduceRow(i)
            count += self.reduceCol(i)
            count += self.reduceCell(i // 3, i % 3)
        print("removed {} possible values.".format(count))
        return count

    def reduceAll(self):
        while self.reduceBoard() > 0:
            pass

    def solved(self):
        toSolve = 81
        solvable = True
        for x in self.field:
            for y in x:
                if isinstance(y, list):
                    if len(y) == 0:
                        solvable = False
                else:
                    toSolve -= 1
        return solvable, toSolve


def main(**kwargs):
    pre = [(0, 0, 8), (1, 2, 3), (1, 3, 6),
           (2, 1, 7), (2, 4, 9), (2, 6, 2),
           (3, 1, 5), (3, 5, 7), (4, 4, 4),
           (4, 5, 5), (4, 6, 7), (5, 3, 1),
           (5, 7, 3), (6, 2, 1), (6, 7, 6),
           (6, 8, 8), (7, 2, 8), (7, 3, 5),
           (7, 7, 1), (8, 1, 9), (8, 6, 4)]
    sudoku = Sudoku(pre)
    # [(1, 1, 1), (1, 2, 2), (0, 0, 3), (0, 6, 8), (3, 2, 5)]
    # sudoku.printGrid()
    # sudoku.reduceAll()
    # sudoku.printGrid()
    running = True
    while running:
        sudoku.reduceAll()
        sudoku.printGrid()

        toSolve, solvable = sudoku.solved()
        if toSolve > 0:


        x = int(input("[x]> "))
        y = int(input("[y]> "))
        if isinstance(sudoku.field[x][y], list):
            print("Possible values: {}".format(sudoku.field[x][y]))
            v = int(input("[value]> "))
            old = sudoku.field[x][y]
            sudoku.field[x][y] = v
            if "y" not in input("[okya]> ").lower():
                sudoku.field[x][y] = old
        else:
            print("no need to change it!")


if __name__ == "__main__":
    main()