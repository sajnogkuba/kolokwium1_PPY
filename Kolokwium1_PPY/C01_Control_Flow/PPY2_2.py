# wyniki wypisz na konsoli
def printNumbers(number):
    for i in range(number, number + 10):
        print(i, end=" ")


def printNumbersToX(number):
    for i in range(number + 1):
        print(i, end=' ')


def multiplicationTable(number):
    even = []
    odd = []
    for i in range(21):
        multiply = number * i
        even.append(multiply) if multiply % 2 == 0 else odd.append(multiply)
    print("even:", "       ", "odd:")
    for i in range(len(even) - 1):
        print(even[i], "       ", odd[i])


# 2A.
# Wypisz 10 następnych liczb naturalnych od wskazanej liczby (wyłącznie). 
# Przykład, number = 5, wyświetl od 5 do 14
printNumbers(5)
print()

# 2B.
# Napisz program, który będzie zwracał tabliczkę mnożenia (do 20.) dla podanej liczby 
# UWAGA-w dwóch kolumnach, moe być w podziale parzyste/nieparzyste
multiplicationTable(5)


# 2C.
# Pobierz od użytkownika liczbę (pomińmy sprawdzanie, czy to liczba, póki co...)
# dodaj do niej wszystkie liczby w zakresie od 0 do tej liczby (włącznie!)
printNumbersToX(20)
