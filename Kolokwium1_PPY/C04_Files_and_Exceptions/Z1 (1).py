# -*- coding: utf-8 -*-


"""
1. Utwórz katalog o nazwie zajęcia
2. Do pliku dzis.txt zapisz dzisiejszą datę
3. Przenieść plik dzis.txt do katalogu zajęcia
4. Utwórz listę integeórw z w zakresie 1-15.
5. Do pliku liczby.txt w katalogu zajęcia zapisz liczby z utworzonej listy, ale tak, aby każdy był w nowej linijce.
Upewnij się, że dane nie zostały nadpisane.
6. Do pliku liczby_parzyste.txt zapisz liczby parzyste z utworzonej wcześniej listy, a do pliku liczby_nieparzyste.txt
zapisz liczby nieparzyste z tej listy.
7. Wszystkie te pliki z polecenia 6 umieść w katalogu zajęcia albo przy tworzeniu, albo po zapisaniu do nich.
8. Wyświetl zawartość katalogu zajęcia
"""
import os
import datetime
import random

# wynikiem ma być ["dzis.txt", "liczby.txt", "liczby_nieparzyste.txt", "liczby_parzyste.txt]
if not os.path.exists("./zajęcia"):
    os.mkdir("./zajęcia")
file_dzis = open("./dzis.txt", "w")
file_dzis.write(str(datetime.datetime.now().date()))
file_dzis.close()
os.rename("./dzis.txt", "./zajęcia/dzis.txt")
numbers = list()
for i in range(21):
    numbers.append(random.randint(1, 15))
file_liczby = open("./zajęcia/liczby.txt", "w")
file_liczby_parzyste = open("./zajęcia/liczby_parzyste.txt", "w")
file_liczby_nieparzyste = open("./zajęcia/liczby_nieparzyste.txt", "w")
for number in numbers:
    file_liczby.write(str(number) + "\n")
    if number % 2 == 0:
        file_liczby_parzyste.write(str(number) + "\n")
    else:
        file_liczby_nieparzyste.write(str(number) + "\n")
print(os.listdir("./zajęcia"))
