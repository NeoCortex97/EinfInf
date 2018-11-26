# -*- coding: utf-8 -*-
# Stefan Schmelz Mat.Nr.: 35221810
# Ingo Kehres    Mat.Nr.: 33318235
# Siamak Najafi  Mat-Nr.: 33397081

def infix(tree=[]):
    if len(tree) == 3:
        if isinstance(tree[1], str) and tree[1] in "+-*/" and len(tree[1]) == 1:
            if isinstance(tree[0], int):
                a = str(tree[0])
            else:
                a = printInfix(tree[0])

            if isinstance(tree[2], int):
                b = str(tree[2])
            else:
                b = printInfix(tree[2])
            return "({0} {1} {2})".format(a, tree[1], b)
        else:
            return None
    else:
        return None


def prefix(tree=[]):
    if len(tree) == 3:
        if isinstance(tree[1], str) and tree[1] in "+-*/" and len(tree[1]) == 1:
            if isinstance(tree[0], int):
                a = str(tree[0])
            else:
                a = printPrefix(tree[0])

            if isinstance(tree[2], int):
                b = str(tree[2])
            else:
                b = printPrefix(tree[2])
            return "{0} {1} {2}".format(tree[1], a, b)
        else:
            return None
    else:
        return None


def postfix(tree=[]):
    if len(tree) == 3:
        if isinstance(tree[1], str) and tree[1] in "+-*/" and len(tree[1]) == 1:
            if isinstance(tree[0], int):
                a = str(tree[0])
            else:
                a = printPostfix(tree[0])

            if isinstance(tree[2], int):
                b = str(tree[2])
            else:
                b = printPostfix(tree[2])
            return "{0} {1} {2}".format(a, b, tree[1])
        else:
            return None
    elif len(tree) == 1:
        return str(tree[0])
    else:
        return None


def main():
    print(infix([1, "+", [1, "-", 3]]))
    print(prefix([1, "+", [1, "-", 3]]))
    print(postfix([1, "+", [1, "-", 3]]))


if __name__ == "__main__":
    main()