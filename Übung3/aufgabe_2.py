# -*- coding: utf-8 -*-
from pprint import pprint


def intSuperliste(l=list):
    for i in l:
        if type(i) not in (int, list):
            return False
        elif type(i) == list:
            return intSuperliste(i)
    return True


def kopie(super_list=list):
    is_simple_list = True
    for i in super_list:
        if type(i) == list:
            is_simple_list = False
    if is_simple_list:
        return super_list[:]
    else:
        result = []
        for i in super_list:
            if type(i) == int:
                result.append(i)
            else:
                result.append(kopie(i))
        return result


def main(**kwargs):
    """
    Die mainfunktion soll es ermöglichen einfacher ein bisschen mit den geschriebenen funktionen zu experimentieren
    und ohne die konsole zu testen.
    :param kwargs:
    :return:
    """
    print("An exercise for int Superlists. ")
    end = False
    # mainloop um mehrere operationen in einem durchlauf zu machen
    liste = []
    while not end:
        op = input("[COMMAND](print/append/list/help/clear/check/EXIT)> ")
        if op.lower() in "print":
            pprint(liste)
        elif op.lower() in "append":
            liste.append(int(input("[VALUE]> ")))
        elif "list" in op.lower():
            params = op.split(" ")[1:]
            tmp = []

            for p in params:
                tmp.append(int(p))
            liste.append(tmp)
        elif op.lower() in "help":
            print("print == liste ausgeben\nappend == zahl anfügen\nlist == Liste anfügen\n" +
                  "help == diese Nachricht anzeigen\nclear == liste leeren\n" +
                  "check == Püfen ob liste eine superliste ist\nexit == beenden")
        elif op.lower() in "clear":
            liste.clear()
        elif op.lower() in "check":
            if intSuperliste(liste):
                print("Jap")
            else:
                print("Nope")
        if op.lower() in "exit":
            end = True


if __name__ == "__main__":
    main()
