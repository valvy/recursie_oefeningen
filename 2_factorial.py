def factorial(n: int) -> int:
    """
    5 = 5 * 4 * 3 * 2 * 1
    4 = 4 * 3 * 2 * 1
    3 = 3 * 2 * 1
    Gebruik hiervoor recursie!
    :param n: getal waarvan je faculteit uitrekent
    :return:
    """
    pass

def testFactorial(getal, vermoeden):
    resultaat = factorial(getal) == vermoeden
    if not resultaat: print("Code klopt niet!!!!")
    else: print("getal {} komt {} door de test".format(getal, "" if vermoeden else "niet" ))

testFactorial(0,1)
testFactorial(1,1)
testFactorial(2,2)
testFactorial(3,6)
testFactorial(6,720)
testFactorial(10,3628800)