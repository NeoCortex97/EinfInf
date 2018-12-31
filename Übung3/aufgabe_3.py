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
        if 0 < v < result:
            result = v
    return result


def get_smallest_tree(height=float()):
    rule1, calculated1 = cond_eins(height)
    rule2, calculated2 = cond_zwei(height)

    if not (calculated1 and calculated2):
        print(rule1, rule2, calculated2 or calculated1)
        return min(rule1, rule2)
    else:
        extra = get_smallest_tree(max(rule1, rule2))
        return min(rule1, rule2, extra)

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