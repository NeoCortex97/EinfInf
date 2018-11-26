# -*- coding: utf-8 -*-
import sys


def lies_zeile(text=""):
    """

    :param text:
    :return:
    """
    if text.count(",") == 2:
        title = ""
        actor = ""
        regiseur = ""
        pos = 0
        for c in text:
            if c == ",":
                pos += 1
            elif pos == 0:
                title += c
            elif pos == 1:
                actor += c
            elif pos == 2:
                regiseur += c
        return title, actor, regiseur
    else:
        return None


def lies_datei(file):
    """

    :param file:
    :return:
    """
    result = list()
    line = file.readline()
    while line != "":
        tmp = lies_zeile(line)
        if tmp is not None:
            result.append(tmp)
        else:
            return None
        line = file.readline()
    return result


def hat_schauspieler(films=list(), text=""):
    """

    :param films:
    :param text:
    :return:
    """
    for t in films:
        if t[1] == text:
            return True
    return False


def schauspieler_zusammenarbeit(films=list(), actor=""):
    """

    :param films:
    :param actor:
    :return:
    """
    if hat_schauspieler(films, actor):
        films = []
        result = []
        for f in films:
            if f[1] == actor:
                films.append(f[0])
            if f[0] in films:
                result.append(f[1])
        return result
    else:
        return None


def fuege_ein(films=list(),entry=("", "", "")):
    """

    :param films:
    :param entry:
    :return:
    """
    index = 0
    result = []
    for f in films:
        if entry[2] == f[2]:
            result.extend(films[:index])
            result.append(entry)
            result.extend(films[index:])
            return result
    return None


def main(**kwargs):
    """
    uses **kwars, so i can place the file outside of the scripts directory if i want to.
    :param kwargs:
    :return:
    """
    print("A task to practice working with tuples. \nMain function serves to play with the functions.")
    try:
        file = open("hollywood.csv")
    except IOError:
        file = open(kwargs["basepath"] + "hollywood.csv")
    print("reading file . . .")
    films = lies_datei(file)
    end = False
    while not end:
        # the main loop to allow multiple operations in one execution
        op = input("[OPERATION](contains/collab/insert/QUIT)> ")
        if op.lower() in  "quit":
            end = True
        elif op.lower() in "contains":
            print("Test if an actor is in the database.")
            hat_schauspieler(films, input("[ACTOR]> "))
        elif op.lower() in "collaboration":
            result = schauspieler_zusammenarbeit(films, input("[ACTOR]> "))
            sys.stdout.write("|")
            count = 1
            for a in result:
                sys.stdout.write("{:40}|".format(a))
                if count == 5:
                    sys.stdout.write("\n")
                    count = 0
                count += 1
        elif op.lower() in "insert":
            actor = input("[ACTOR]> ")
            title = input("[TITLE]> ")
            regiseur = input("[REGISEUR]> ")
            fuege_ein(films, (title, actor, regiseur))
        else:
            print("It seems that there is nothing i can do about " + op)


if __name__ == "__main__":
    main()
