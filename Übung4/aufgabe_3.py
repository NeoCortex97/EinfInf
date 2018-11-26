# -*- coding: utf-8 -*-
# Stefan Schmelz Mat.Nr.: 35221810
# Ingo Kehres    Mat.Nr.: 33318235
# Siamak Najafi  Mat-Nr.: 33397081

def readWallet(vals=[]):
    print("Wie sieht dein Geldbeutel aus?")
    result= []
    for val in vals:
        result. append(int(input("Wie viele {0:>3}€ Münzen hast du im Geldbeutel?\n> ".format(val))))
    return result


def canBePayed(vals=[], stock=[], amount=int()):
    stockValue = 0
    for i in range(len(vals)):
        stockValue += vals[i] * stock[i]
    if amount <= stockValue:
        return True
    return False


def checkNonBacktracking(vals=[], stock=[], amount=int()):
    stillToPay = amount
    result = []
    idx = len(stock) - 1
    for a in reversed(vals):
        count = int(stillToPay / a)
        if stock[idx] >= count:
            result.append(count)
            stillToPay = stillToPay % a
        idx -= 1
    if stillToPay == 0:
        return result
    return []


def getCount(coin, value):
    count = int(value / coin)
    return count, value - (count * coin)


def check(vals=[], stock=[], amount=0, convert=True):
    result = []
    for i in vals:
        # print("Testing ", i)
        if amount >= i and stock[vals.index(i)] > 0:
            result.append(i)
            stock[vals.index(i)] -= 1
            amount -= i
            result.extend(check(vals, stock, amount, False))
            if amount == 0:
                break
            else:
                result.append(-1)

    if convert:
        counter = []
        # print(result)
        if result.count(-1):
            for i in vals:
                a = result.count(i)
                if a > 0:
                    counter.append(result.count(i))
                else:
                    counter.append(int("0"))
                # print(counter)
                return counter
        else:
            return None
    else:
        return result


def main():
    vals= [25, 17, 11, 6]
    stock = readWallet(vals)
    amount = int(input("Wie viel musst du bezahlen?\n> "))
    if canBePayed(vals, stock, amount):
        print("Du hast theoretisch genug geld um das zu bezahlen.")
        result = check(vals, stock, amount)
        if result is not None:
            for i in range(len(vals)):
                try:
                    print("du brauchst {0} mal {1}€.".format(result[i], vals[i]))
                except IndexError:
                    print("du brauchst 0 mal {0}€.".format(vals[i]))
        else:
            print("Das ist mit deinem Inhalt nicht möglich!")


if __name__ == "__main__":
    main()