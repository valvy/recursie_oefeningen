#!/usr/bin/env python3

def convert_decimal_to_binary(decimal: int) -> str:
    """
    Converteer een decimaal getal recursief naar een binair getal.
    Dat doe je door de volgende rekensom.
    Is het getal oneven, haal er 1 van af en deel het door twee. (Bewaar de 1)
    Is het getal even, haal er 0 van af en deel het door twee
    Blijf doorgaan tot het getal 0 is.
    Voorbeeld: 10
    10 / 2 = 5, 10 is even dus 0
    5 / 2 = 2, 5 is oneven dus 1
    2 / 2 = 1, 1 is even dus 0
    1 / 1 = 0, 1 is oneven dus 1
    antwoord = 10 = 0101 (of 101 aangezien de 0 aan het begin niet meetelt)
    """
    if decimal <= 1:
        return str(decimal)
    return convert_decimal_to_binary(decimal // 2) + str(decimal % 2)


def test_decimal_to_binary(getal, assertie):
    resultaat = convert_decimal_to_binary(getal)
    if not assertie == resultaat:
        print("code klopt niet!")
    else:
        print("getal {} komt {} door de test".format(getal, "" if resultaat else "niet"))


test_decimal_to_binary(125, "1111101")
test_decimal_to_binary(5, "101")
test_decimal_to_binary(6, "110")
test_decimal_to_binary(6134224, "10111011001100111010000")
