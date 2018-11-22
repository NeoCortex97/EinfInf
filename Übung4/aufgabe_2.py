def printInfix(tree=[]):
    if len(tree) == 3:
        if isinstance(tree[1], str):
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


def printPrefix(tree=[]):
    if len(tree) == 3:
        if isinstance(tree[1], str):
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


def printPostfix(tree=[]):
    if len(tree) == 3:
        if isinstance(tree[1], str):
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
    print(printInfix([1, "+", [1, "-", 3]]))
    print(printPrefix([1, "+", [1, "-", 3]]))
    print(printPostfix([1, "+", [1, "-", 3]]))


if __name__ == "__main__":
    main()