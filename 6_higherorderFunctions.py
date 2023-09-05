#!/usr/bin/env python3

import functools

# Een higher order function is een functie die een functie als parameter of return heeft
# Neem het voorbeeld map:
def my_map(func: callable, my_list: []) -> []:
    """
    Met map lus je door alle waardes heen van een lijst,
    Deze waardes transformeer je d.m.v. een functie
    @param func => Een functie waarmee je een waarde wilt transformeren
    @param my_list => De lijstje waar je alle waardes van wilt transformeren
    """
    tail = my_list[:1]
    return [] \
        if len(tail) == 0 \
        else [func(tail[0])] + my_map(func, my_list[1:])


# Alle waardes wordt een opgehoogd (Lambda is een anonieme functie)
print(
    my_map(lambda d: d + 1,
           [1, 3, 4]))


# Een andere higher order function is de filter functie:
def my_filter(func: callable, my_list: []) -> []:
    """
        Hier moet de func (de functie die je meegeeft) => Een waarde true of false terug geven.
        Wanneer de functie de waarde true geeft, neem het niet op in de list
        Als de waarde aan een bepaalde conditie voldoet, filter deze er dan uit
    """
    pass

def test_code_filter(
        my_list,
        func,):
    gekregen = my_filter(func, my_list)
    verwacht = list(filter(func, my_list))
    resultaat = gekregen == verwacht
    if not resultaat:
        print(f"gegeven {gekregen} verwacht {verwacht}")
        print("Code klopt niet!!!!")
    else:
        print("Code klopt!")


test_code_filter(
    [0, 2, 3, 4, 5],
    lambda x: x > 3
)

test_code_filter(
    [0, 2, 3, 4, 5],
    lambda x: x < 3
)

test_code_filter(
    [0, 2, 3, 4, 5],
    lambda x: True
)


def my_reduce(func, my_list: [], start_value):
    """
    De reduce functie combineerd bepaalde waarden met elkaar.
    Gegeven is een functie die een operatie doet op alle elementen tot er nog maar 1 element over is
    Bijvoorbeeld de input [1,2,3,4,5], lambda x, y: x + y, 0
    Hierbij worden alle elementen bij elkaar opgeteld. (1 + 2 + 3 + 4 + 5)
    """
    pass


def test_code_reduce(
        my_list,
        func, start):
    gekregen = my_reduce(func, my_list, start)
    verwacht = functools.reduce(func, my_list, start)
    resultaat = gekregen == verwacht
    if not resultaat:
        print(f"gegeven {gekregen} verwacht {verwacht}")
        print("Code klopt niet!!!!")
    else:
        print("Code klopt!")


test_code_reduce([1,2,3,4,5], lambda x, y: x + y, 0)

test_code_reduce([1,2,3,4,5], lambda x, y: f"{x} : {y}", "")

