# -*- coding: utf-8 -*-
"""

Napisz definicję, która przeprowadzi analizę tekstu. Program powinien wykonać następujące czynności:
- Wczytać tekst
- Podzielić tekst na słowa.
- Usunąć znaki interpunkcyjne i zamienić wszystkie litery na małe litery.
- Utworzyć kolekcję słów i zliczyć ile razy każde słowo występuje w tekście.
- Wyświetlić 10 najczęściej występujących słów wraz z ich liczbami wystąpień.
- Wyświetlić 10 najrzadziej występujących słów wraz z ich liczbami wystąpień.
- Wyświetlić liczbę unikalnych słów w tekście.
- Wyświetlić średnią długość słowa w tekście.
"""


def averageWordLength(text):
    words = text.split()
    amount_of_letters = 0
    for word in words:
        amount_of_letters += len(word)
    return amount_of_letters / len(words)


def analyseFile(file_name):
    file = open(file_name, "r")
    text = file.read()
    text = text.lower().replace('.', "").replace(',', "")
    words = text.split()
    number_of_appearances = dict()
    for word in words:
        if word in number_of_appearances:
            number_of_appearances[word] = number_of_appearances[word] + 1
        else:
            number_of_appearances[word] = 1
    entries_list = sorted(number_of_appearances.items(), key=lambda x: x[1], reverse=True)
    print("10 most popular words:")
    for word, count in entries_list[:10]:
        print('- \"', word, "\" cont: ", count, sep="")
    print()
    entries_list = sorted(number_of_appearances.items(), key=lambda x: x[1])
    print("10 less popular words:")
    for word, count in entries_list[:10]:
        print('- \"', word, "\" cont: ", count, sep="")

    print()
    print("Amount of unique words: ", len(number_of_appearances))
    print("Average word length:", averageWordLength(text))






analyseFile("Z2_txt.txt")
