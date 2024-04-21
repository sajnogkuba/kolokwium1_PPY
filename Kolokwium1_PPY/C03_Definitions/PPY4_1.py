# -*- coding: utf-8 -*-
# Napisz funkcje silnii używając rekurencji

def factorialRecursive(number: int) -> int:
    if number == 1:
        return number
    else:
        return number * factorialRecursive(number - 1)


print(factorialRecursive(6))
