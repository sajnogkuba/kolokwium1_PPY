# -*- coding: utf-8 -*-
"""
Napisz funkcję, która przyjmuje dowolną ilość liczb (args*) i znaków działania (kwargs**), gdzie znakami działania mogą
być: '+', '-', '*', '/'
Funkcja ma zwracać wynik działania na liczbach
"""
from unittest import case


def kalkulator(*args, **kwargs):
    result = 0
    match kwargs["działanie_1"]:
        case "+": result = args[0] + args[1]
        case "-": result = args[0] - args[1]
        case "*": result = args[0] * args[1]
        case "/": result = args[0] / args[1]
    for i in range(1, len(kwargs)):
        match kwargs[f"działanie_{i + 1}"]:
            case "+":
                result += args[i + 1]
            case "-":
                result -= args[i + 1]
            case "*":
                result *= args[i + 1]
            case "/":
                result /= args[i + 1]
    return result


# Przykładowe użycie funkcji
print(kalkulator(10, 8, 2, 2, działanie_1='*', działanie_2="+", działanie_3="/"))  # 82
