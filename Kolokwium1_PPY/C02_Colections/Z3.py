# -*- coding: utf-8 -*-
"""
Napisz program, który umożliwia zarządzanie książką adresową. Program powinien umożliwiać użytkownikowi
wykonywanie następujących operacji:

Dodawanie nowego kontaktu do książki adresowej.
Wyświetlanie wszystkich kontaktów z książki adresowej.
Wyszukiwanie kontaktu po nazwie.
Usuwanie kontaktu z książki adresowej.

Użyj słownika, gdzie kluczem będzie nazwa kontaktu, a wartością będzie lista informacji o kontakcie (np. imię,
nazwisko, numer telefonu).
"""


def userInputChoice(options_list):
    correct_input = False
    user_input = 0
    while not correct_input:
        try:
            user_input = int(input())
        except ValueError:
            user_input = 0
        if user_input in options_list:
            correct_input = True
        else:
            print('Invalid choose, try again')
    return user_input


phone_book = dict()
print('What would you like to do?:')
print('\t 1. Add a phone number')
print('\t 2. See all phone numbers')
print('\t 3. Search a phone number')
print('\t 4. Delete a phone number')
