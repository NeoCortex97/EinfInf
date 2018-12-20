# Aufgabe 3:
#
# a)

def hat_schlaufe(buch, i):
    if buch[i] == i:
        return True
    else:
        return False


#
# Welche Laufzeit hat Ihre Funktion, und warum?
#   Die Laufzeit ist O(1), da der zugriff im Wörterbuch eine konstante Zeit benötigt
#
#
#
#
#

# b)

def laenge(buch, i):
    if hat_schlaufe(buch, i):
        return 1
    else:
        return laenge(buch, buch[i]) + 1


#
# Welche Laufzeit hat Ihre Funktion, und warum?
#   Worst case: O(n)
#   weil der ganze pfad, dessen länge als n definiert ist durchlaufen werden muss
#
#
#
#

# c)

def eintrag(buch, i, j):
    if j < laenge(buch, i):
        result = buch[i]
        for index in range(j - 1):
            result = buch[result]
        return result
    else:
        return -1


#
# Welche Laufzeit hat Ihre Funktion, und warum?
#   O(n)
#   Weil zu der linearen laufzeit von laenge noch j operationen hinzu kommen, aber diese ignoriert werden können
#
#
#
#

# d)

def verlaengere(buch, i, j):
    if i != j:
        pos = i
        while not hat_schlaufe(buch, pos):
            if buch[pos] == j:
                return False
            pos = buch[pos]
        buch[pos] = j
        return True
    else:
        return False


#
# Welche Laufzeit hat Ihre Funktion, und warum?
#   O(n)
#   m ist irrelevant, da nur j und nicht dessen länge benötigt wird.
#   n muss komplett durchlaufen werden
#
#
#

# e)

def pfad(buch, i):
    pos = i
    result = list()
    while not hat_schlaufe(buch, pos):
        result.append(buch[pos])
        pos = buch[pos]
    return result


def disjunkt(buch, i, j):
    a = pfad(buch, i)
    b = pfad(buch, j)
    for item in a:
        if item in b:
            return False
    return True

#
# Welche Laufzeit hat Ihre Funktion, und warum?
#   O(n + m + n*m)
#   Weil der komplette pfad n durchlaufen wird
#   und der komplette pfad m durchlaufen wird
#   und dann für jedes element aus n jeses element von m durchlaufen wird
#
#







# Nicht veraendern!
if __name__ == '__main__':
# Ihren globalen Testcode koennen Sie hier platzieren:
    buch = {0: 0, 1: 3, 2: 2, 3: 4, 4: 4, 5: 2, 6: 8, 7: 6, 8: 8}
    print("Hat schlaufe bei 0 ist True: {}".format(str(hat_schlaufe(buch, 0) == True)))
    print("Hat schlaufe bei 1 ist False: {}".format(str(hat_schlaufe(buch, 1) == False)))
    print("laenge von 0 ist 1: {}".format(str(laenge(buch, 0) == 1)))
    print("laenge von 6 ist 2: {}".format(str(laenge(buch, 6) == 2)))
    # print("laenge von 6 ist: {}".format(laenge(buch, 6)))
    # print("laenge von 1 ist: {}".format(laenge(buch, 1)))
    print("eintrag von 1 | 1 ist 3: {}".format(str(eintrag(buch, 1, 1) == 3)))
    # print("eintrag von 1 | 1 ist: {}".format(eintrag(buch, 1, 1)))
    print("eintrag von 5 | 2 ist -1: {}".format(str(eintrag(buch, 5, 2) == -1)))
    # print("eintrag von 5 | 2 ist: {}".format(eintrag(buch, 5, 2)))
    print("verlaengere 1 | 5 ist True: {}".format(str(verlaengere(buch, 1, 5) == True)))
    print("verlaengere 1 | 4 ist False: {}".format(str(verlaengere(buch, 1, 4) == False)))
    print("disjunkt von 6 | 7 ist False: {}".format(str(disjunkt(buch, 6, 7) == False)))
    print("disjunkt von 5 | 8 ist True: {}".format(str(disjunkt(buch, 5, 8) == True)))


