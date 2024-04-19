# -*- coding: utf-8 -*-

"""
Napisz funkcję słowa_podobne (s, words), która wyświetli słowa, które są ""podobne" do napisu s
w tym sensie, że składające się z tych samych znaków — ale ewentualnie występujących inną liczbę razy
#PRZYKŁAD
słowa_podobne ('one', ['one', 'two', 'none', 'three', 'neon', 'eon'])
» none neon eon
"""


def getLettersSet(word):
    set_of_letters = set()
    for letter in word:
        set_of_letters.add(letter)
    return set_of_letters


def similarWords(s, words):
    result = list()
    base_set = getLettersSet(s)
    for word in words:
        if base_set == getLettersSet(word) and s != word:
            result.append(word)
    for word in result:
        print(word, end=' ')


similarWords('one', ['one', 'two', 'none', 'three', 'neon', 'eon'])
