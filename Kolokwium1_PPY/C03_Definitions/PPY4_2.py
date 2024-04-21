# -*- coding: utf-8 -*-
"""
Napisz funkcje validate_pesel, która przyjmuje ciąg znaków (str) i sprawdza, czy jest on poprawnie sformatowanym
numerem PESEL. Numer PESEL składa się z 11 cyfr. W celu sprawdzenia sumy kontrolnej użyj wag [1, 3, 7, 9, 1, 3, 7, 9,
1, 3]. Tutaj suma kontrolna to wynik odejmowania jedności od 10. Funkcja powinna zwracać wartość logiczną: True, jeśli
numer PESEL jest poprawny, False w przeciwnym przypadku.
"""


def validate_pesel(pesel):
    if not pesel.isnumeric() or pesel.__len__() != 11:
        return False
    else:
        wights = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
        correct_last_digit = 0
        for i in range(len(pesel) - 1):
            correct_last_digit += (int(pesel[i]) * wights[i])
        correct_last_digit = 10 - correct_last_digit % 10
        return correct_last_digit == int(pesel[-1])


print(validate_pesel('12345678901'))  # False
print(validate_pesel('44051401458'))  # True
