# Aufgabe 2:
#
# a) Wie berechnet das Programm die angegebene Funktion?
#   max gibt 0 zurück, wenn es eine leere liste bekommt.
#   Anderenfalls testet sie ob das erste Element der Liste (index 0) größer ist als das maximum der restlichen liste.
#   für die Berechnung des Maximums der restlichen liste wird ebenfalls die Funktion Max benutzt.
#
#   maxmult gibt 0 zurück, wenn die länge von L kleiner 2 ist.
#   dann wird das größter Produkt der restlichen liste berechnet (maxmult).
#   und das produkt des ersten Elements mit dem größten Element (max).
#   es wird das ergebnis von maxmult zurückgegeben, wenn es größer ist, als das produkt des ersten elements mit dem größten element.
#
#
#
#
#
# b) Was ist die Laufzeit des Programms, und warum ist das so?
#   O(n^4)
#
#
#
#
#
#
#
#
#
#
#
#

# c)
#  Ihre Loesung:
#
def maxmult_lin(L):
    if len(L) < 2:
        return 0
    elif len(L) == 2:
        return sum(L)
    else:
        a, b = 0, 0
        for i in L:
            if i > a:
                a,b = i, a
            elif i > b:
                b = i
        return a * b








# Nicht veraendern!
if __name__ == '__main__':
# Ihren globalen Testcode koennen Sie hier platzieren:
    print("Bei eingabe von [2, 6, 4] sollte 24 zürückgegeben werden: {}".format(str(maxmult_lin([2, 6, 4]) == 24)))
    print("Bei Eingabe von [2, 6, 8, 1, 8] sollte 64 zurückegegeben werden: {}".format(str(maxmult_lin([2, 6, 8, 1, 8]) == 64)))
