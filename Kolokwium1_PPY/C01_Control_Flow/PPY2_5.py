# napisz program, który zwróci wszystkie liczby pierwsze dla wybranego zakresu
# Podpowiedź-znajdź warunki, które eliminują kryteria liczby pierwszej.

from math import sqrt


def primeNumbersInRange(range_start, stop):
    primenumbers = []
    dives = 0
    for j in range(range_start, stop + 1):
        for k in range(1, int(sqrt(j)) + 1):
            if j % k == 0:
                dives += 1
        if dives <= 1 and j not in [0, 1]:
            primenumbers.append(j)

        dives = 0

    return primenumbers


start = 1073
end = 10735
print("Liczby pierwsze pomiędzy", start, "i", end, "to:")
primeNumbersInRange(start, end)

for i in primeNumbersInRange(start, end):
    print(i, sep=" ")
