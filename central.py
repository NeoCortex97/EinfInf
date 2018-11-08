# -*- coding: utf-8 -*-
import sys
import os
import importlib
import traceback


def print_line(line=list(), width=int(), count=int()):
    sys.stdout.write("\x1B[31;2m│")
    for i in range(count):
        if i < len(line):
            sys.stdout.write(("\x1B[33;1m{:^" + str(width) + "}").format(line[i]) + "\x1B[31;22m│\x1B[0m")
        else:
            sys.stdout.write(("{:^" + str(width) + "}").format(" ") + "\x1B[31m│\x1B[0m")
    sys.stdout.write("\n")


def longest_entry(array):
    result = 0
    for a in array:
        if result < len(a):
            result = len(a)
    return  result


def print_table(lines, width):
    count = longest_entry(lines)
    print("\x1B[31;2m╒" + ("═" * width) + (("╤" + ("═" * width)) * (count - 1)) + "╕\x1B[0m")
    print_line(lines[0], width, count)
    for i in range(1, len(lines)):
        print("\x1B[31;2m╞" + ("═" * width) + (("╪" + ("═" * width)) * (count - 1)) + "╡\x1B[0m")
        print_line(lines[i], width, count)
    print("\x1B[2;31m╘" + ("═" * width) + (("╧" + ("═" * width)) * (count - 1)) + "╛\x1B[0m")


def get_path_contents(path, pattern):
    raw = os.listdir(path)
    result = []
    for i in raw:
        if pattern in i:
            result.append(i)
    return result


def get_pattern_from_filesystem(basepath, first_key, second_key):
    dirs = get_path_contents(basepath, first_key)
    result = list()
    for d in dirs:
        result.append(list())
        result[-1].append(d)
        contents = get_path_contents(basepath + "/" + d, second_key)
        for f in contents:
            result[-1].append(f)
    return result


def format_pattern(pattern):
    result = list()
    l = longest_entry(pattern)
    result.append(list())
    result[0].append("Übung")
    for i in range(1, l):
        result[0].append("Aufgabe " + str(i))
    for row in pattern:
        result.append(list())
        for i in row:
            if "Übung" in i:
                result[-1].append(i[5:])
            else:
                result[-1].append("{0:02}".format(int(result[-1][0])) + "{0:02}".format(int(i[8:-3])))
    return result


def import_and_run(pattern, which):
    übung = pattern[int(which[:2]) - 1][0]
    aufgabe = pattern[int(which[:2]) - 1][int(which[2:])].strip(".py")
    # print("Übung bei " + which[:2] + "ist " + übung)
    # print("aufgabe bei " + which[2:] + "ist " + aufgabe)
    try:
        mod = importlib.import_module(übung + "." + aufgabe)
        func = getattr(mod, "main")
        func(**{"basepath": (übung + "/")})
        del mod
    except Exception:
        traceback.print_exc()


def process_command(pattern, command, width):
    if command.lower() in "help":
        print("exit     == end program")
        print("help     == print this message")
        print("list     == list all available programms.")
        print("run XXXX == execute the program of this task")
    elif command.lower() in "exit":
        return True
    elif "run " in command.lower():
        import_and_run(pattern, command[4:])
    elif command.lower() in "list":
        print_table(format_pattern(pattern), width)
    else:
        print("You entered an unknown command!\nPlease check syntax.")
    return False


def main():
    print("Homework browser")
    cell_width = 15
    # lines = [["Übung", "Aufgabe 1", "Aufgabe 2", "Aufgabe 3", "Aufgabe 4", "Aufgabe 5", "Aufgabe 6", "Aufgabe 7"],
    #          [" 1", "0101", "0102", "0103", "0104", "0105", "0106", "0107"],
    #          [" 2", "0201", "0202", "0203", "0204"], [" 3"], [" 4"], [" 5"],
    #          [" 6"], [" 7"], [" 8"], [" 9"], ["10"], ["11"], ["12"]]
    files = get_pattern_from_filesystem(".", "Übung", "aufgabe_")
    lines = format_pattern(files)
    print_table(lines, cell_width)
    finish = False
    while not finish:
        command = input("> ")
        finish = process_command(files, command, cell_width)


if __name__ == "__main__":
    main()