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

"""
tutaj lepiej by było zastosować jakąś klasę PhoneBook i nie przekazywać tej mapy phone_book wszędzie, tylko 
wywoływać metody klasy, ale już zrobiłem jak na ćwiczeniach :P
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


is_running = True
phone_book = dict()


def showAllContacts(phone_book):
    for key, value in phone_book.items():
        print(f'{key}: {value}')


def addContact(phone_book):
    pass


def searchContact(phone_book):
    pass


def deleteContact(phone_book):
    pass


while is_running:
    print('What would you like to do?:')
    print('\t 1. Add a contact')
    print('\t 2. Show all contacts')
    print('\t 3. Search a contact')
    print('\t 4. Delete a contact')
    print('\t 5. Close program')

    user_choice = userInputChoice([1, 2, 3, 4, 5, 6])
    if user_choice == 1:
        addContact(phone_book)
    elif user_choice == 2:
        showAllContacts(phone_book)
    elif user_choice == 3:
        searchContact(phone_book)
    elif user_choice == 4:
        deleteContact(phone_book)
    elif user_choice == 5:
        is_running = False
