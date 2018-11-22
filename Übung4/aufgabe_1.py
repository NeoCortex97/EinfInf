def isTree(tree=[]):
    if len(tree) == 3:
        if not isinstance(tree[1], int):
            return False
        else:
            result = True
            if isinstance(tree[0], int):
                result = True
            elif isinstance(tree[0], list):
                result = isTree(tree[0])
            else:
                return False

            if isinstance(tree[2], int):
                result = True
            elif isinstance(tree[2], list):
                result = isTree(tree[2])
            else:
                result = False
            return result
    else:
        return False

def summiere(tree=[], level=1):
    result = 0
    for i in range(3):
        if isinstance(tree[i], int):
            result += tree[i] * level
        else:
            result = int(result) + int(summiere(tree[i], level + 1))
    return result

def main():
    print(isTree([1, 2, [3, 4, [5, 6, 7]]]))
    print(summiere([1, 2, [3, 4, [5, 6, 7]]]))


if __name__ == "__main__":
    main()