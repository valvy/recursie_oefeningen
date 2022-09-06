#!/usr/bin/env python3

def convert_decimal_to_binary(decimal: int) -> str:
    if decimal <= 1:
        return str(decimal)
    else:
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
