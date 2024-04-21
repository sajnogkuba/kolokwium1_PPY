# -*- coding: utf-8 -*-
"""
Napisz funkcje o nazwie calculate_statistics, która przyjmuje dowolną liczbę argumentów liczbowych oraz str
określający typ operacji ("mean", "median" lub "mode") Funkcja ma obliczyć i zwrócić wynik wybranego działania Użyj
funkcji match case
"""


def calculate_statistics(operation, *args):
    match operation:
        case "mean":
            sum = 0
            for i in args:
                sum += i
            return sum / len(args)
        case "median":
            if len(args) % 2 == 1:
                return args[len(args) // 2]
            else:
                return (args[len(args) // 2] + args[(len(args) // 2) - 1]) / 2
        case "mode":
            result = list()
            count = dict()
            for i in args:
                if i not in count:
                    count[i] = 1
                else:
                    count[i] += 1
            max_count_value = max(count.values())
            for key, value in count.items():
                if value == max_count_value:
                    result.append(key)
            return result

# Przykładowe użycie funkcji
print(calculate_statistics("mean", 1, 2, 3, 4, 5))  # 3.0
print(calculate_statistics("median", 1, 2, 3, 4, 5))  # 3
print(calculate_statistics("mode", 1, 2, 2, 3, 3, 3))  # [3]
