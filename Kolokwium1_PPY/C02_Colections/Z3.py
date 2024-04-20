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
import string

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
    if len(phone_book) == 0:
        print('No contacts to show')
    else:
        print("Your contacts:")
        for key, value in phone_book.items():
            print(f'\t - {key}: {value}')


def formatPhoneNumber():
    phone_number = input('Enter phone number: ')
    for i in range(len(phone_number)):
        if phone_number[i] not in string.digits:
            print('Invalid phone number, try again')
            return formatPhoneNumber()
    return phone_number


def addContact(phone_book):
    contact_name = input('Enter contact name: ')
    name = input('Enter name: ')
    name = name.capitalize()
    surname = input('Enter surname: ')
    surname = surname.capitalize()
    phone_number = formatPhoneNumber()
    if contact_name not in phone_book:
        phone_book[contact_name] = [name, surname, phone_number]
        print('Contact added')
    else:
        print(f'Contact with name {contact_name} already exists, do you want to overwrite it?')
        print('\t 1. Yes')
        print('\t 2. No')
        user_choice = userInputChoice([1, 2])
        if user_choice == 1:
            phone_book[contact_name] = [name, surname, phone_number]
            print('Contact overwritten')
        elif user_choice == 2:
            print('Close operation')
    pass


def searchContact(phone_book):
    name_search = input('Enter search contact name: ')
    if name_search in phone_book:
        print('Found contact with name \"', name_search, '\"->', phone_book[name_search])
    else:
        print('Contact with name \"', name_search, '\" does not exist')


def deleteContact(phone_book):
    name_search = input('Enter contact name to delete: ')
    if name_search in phone_book:
        print('Contact with name', name_search, 'deleted')
    else:
        print('Contact with name', name_search, 'does not exist')
    pass


while is_running:
    print('')
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
