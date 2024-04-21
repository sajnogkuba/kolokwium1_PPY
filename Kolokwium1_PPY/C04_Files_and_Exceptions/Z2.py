# -*- coding: utf-8 -*-

"""
Napisz program, który będzie konwertować temperature między stopniami Celsjusza i stopniami Fahrenheita.
Program powinien pytać użytkownika, na co chce przekonwertować i jaką wartość
Program ma obsługiwać błędy poprzez try i except i kończyć program przy:
    - dzieleniu przez 0
    - wpisaniu przy pytaniu o konwersje coś innego niż F lub C
    - wpisaniu przy pytaniu o wartość coś innego niż int lub float
"""


def userChoiceCF() -> str:
    user_choice = input("What would you like to convert?\n\t C - Celsius to Fahrenheit\n\t F - Fahrenheit to Celsius\n")
    if user_choice not in ["C", "F"]:
        raise ValueError("Invalid choice, you can only choose C or F")
    else:
        return user_choice


is_running = True
while is_running:
    try:
        choice = userChoiceCF()
    except ValueError:
        print("Invalid choice, you can only choose C or F")
        is_running = False
        break

