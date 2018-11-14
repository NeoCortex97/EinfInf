# -*- coding: utf-8 -*-


def cond_eins(height=float()):
    tmp = height - 34
    if tmp > 0:
        return tmp, True
    else:
        return height, False


def cond_zwei(height=float()):
    tmp = (height - 11) / 2
    if tmp > 0:
        return tmp, True
    else:
        return height, False


def min_pos(*args):
    result = args[0]
    for v in args:
        if v > 0 and v < result:
            result = v
    return result


def get_smallest_tree(height=float()):
    rule1, calculated1 = cond_eins(height)
    rule2, calculated2 = cond_zwei(height)
    if rule1 < height:
        result1 = rule1
    else:
        result1 = rule1

    if rule2 < height:
        result2 = rule2
    else:
        result2 = height

    if calculated1 or calculated2:
        return min(get_smallest_tree(result1), get_smallest_tree(result2))
    else:
        return min(result1, result2)

    # tmp1, tmp2 = get_smallest_tree(rule1)
    # tmp3, tmp4 = get_smallest_tree(rule2)
    # if rule1 > 0 and rule2 > 0:
    #     result1 = min_pos(rule1, tmp1, tmp3)
    #     result2 = min_pos(rule2, tmp2, tmp4)

    # return result1, result2

def main(**kwargs):
    print("This programcalculates the smallest tree in \"Habichtswald\" based on following rules:")
    print("1.)  If there is a tree with the height x, there must be a tree of size x - 34")
    print("2.)  If there is a tree with the height x, there must be a tree of size (x - 11) / 2")
    print("smallest tree in the forrest: " + str(get_smallest_tree(float(input("[HEIGHT]> ")))))


if __name__ == "__main__":
    main()