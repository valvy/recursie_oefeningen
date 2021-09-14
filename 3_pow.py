import math


def pow(n: int, p: int) -> int:
    """
    implementeer de math.pow functie
    Gebruik hiervoor recursie!
    :param n:
    :param p:
    :return:
    """
    if p == 0: return 1
    return n if n == 1 else n * pow(n, p - 1)


def testPow(lh,rh):
    resultaat = pow(lh,rh) == int(math.pow(lh,rh))
    if not resultaat:
        print("{} en {} was niet correct met antwoorden {} en {}".format(lh,rh, pow(lh,rh), int(math.pow(lh,rh))))
        print("Code klopt niet!!!!")
    else: print("Code klopt!")

testPow(4,5)
testPow(2,7)
testPow(2,9)
