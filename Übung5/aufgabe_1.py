# -*- coding: utf-8 -*-
# Stefan Schmelz Mat.Nr.: 35221810
# Ingo Kehres    Mat.Nr.: 33318235
# Siamak Najafi  Mat-Nr.: 33397081


<<<<<<< Updated upstream

def main(**kwargs):
    pass

if __name__ == "__main__":
	main()
=======
def filter_paindrom(data=list()):
    return [s for s in data if s != s[::-1]]


def liste_kleiner(liste1=list(), liste2=list()):
    return [min(a,b) for a, b in zip(liste1, liste2)]


def custom_op(liste=list()):
    pure_int = True
    pure_string = True
    for item in liste:
        if isinstance(item, int):
            pure_string = False
        elif isinstance(item, str):
            pure_int = False
        else:
            pure_int = False
            pure_string = False
    if pure_int:
        return [i * 2 for i in liste]
    elif pure_string:
        return [s[::-1] for s in liste]
    else:
        return liste


def sortiere(kleiner,L):
    trenner = 0
    while trenner != len(L):
        for i in range(trenner,len(L)):
            if kleiner(L[i],L[trenner]):
                L[trenner], L[i] = L[i], L[trenner]
        trenner += 1
    return L



def main(**kwargs):
    print("Teilaufgabe 1:")
    print(filter_paindrom(["test", "anna"]))

    print("Teilaufgabe b:")
    print(liste_kleiner([5, 7, -3, -1], [2, 10, -3, 5]))

    print("Teilaufgabe c:")
    L = [[1, 2, 3], ["ab", "3a5"]]
    L2 = list(map(custom_op, L))
    for l in  L2:
        print(l)

    print("Teilaufgabe d:")
    l = ["z", "aaa", "1", "11111", "ccv", "22"]
    print("ausgangsdaten: ", l)
    print(sortiere((lambda x, y: True if len(x) < len(y) else (False if len(x) > len(y) else x < y)), l))


if __name__ == "__main__":
    main()
>>>>>>> Stashed changes
