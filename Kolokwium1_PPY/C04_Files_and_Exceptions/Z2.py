# -*- coding: utf-8 -*-

"""
Napisz program, który będzie konwertować temperature między stopniami Celsjusza i stopniami Fahrenheita.
Program powinien pytać użytkownika, na co chce przekonwertować i jaką wartość
Program ma obsługiwać błędy poprzez try i except i kończyć program przy:
    - dzieleniu przez 0
    - wpisaniu przy pytaniu o konwersje coś innego niż F lub C
    - wpisaniu przy pytaniu o wartość coś innego niż int lub float
"""


def celsius2fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


def fahrenheit2celsius(fahrenheit):
    return ((fahrenheit - 32) * 5) / 9


def userChoiceCF() -> str:
    user_choice = input("What would you like to convert?\n\t C - Celsius to Fahrenheit\n\t F - Fahrenheit to Celsius\n")
    if user_choice not in ["C", "F"]:
        raise ValueError("Invalid choice, you can only choose C or F")
    else:
        return user_choice


is_running = True
while is_running:
    try:
        try:
            choice = userChoiceCF()
        except ValueError:
            print("Invalid choice, you can only choose C or F")
            is_running = False
            break
        try:
            degrees = float(input("Type in value to convert: \n"))
        except ValueError:
            print("Invalid degree value.")
            is_running = False
            break
        match choice:
            case "C":
                converted_degrees = celsius2fahrenheit(degrees)
                print(f"{degrees}°C is {converted_degrees}°F")
            case "F":
                converted_degrees = fahrenheit2celsius(degrees)
                print(f"{degrees}°F is {converted_degrees}°C")
    except ZeroDivisionError:
        print("You can't divide by zero")
