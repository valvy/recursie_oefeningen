
def helloWorld(n: int, word: str):
    """print n keer de hoeveelheid woordjes"""
    if n == 0:
        return
    print(word)
    helloWorld(n-1, word)



helloWorld(10,"test")