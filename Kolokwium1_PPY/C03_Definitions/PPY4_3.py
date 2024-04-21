# -*- coding: utf-8 -*-
#Napisz funkcje o nazwie calculate_statistics, która przyjmuje dowolną liczbę argumentów liczbowych oraz str określający typ operacji ("mean", "median" lub "mode")
#Funkcja ma obliczyć i zwrócić wynik wybranego działania
#Użyj funkcji match case
def calculate_statistics(operation, *args):
  #TWÓJ KOD
  pass

#Przykładowe użycie funkcji
print(calculate_statistics("mean", 1, 2, 3, 4, 5))  # 3.0
print(calculate_statistics("median", 1, 2, 3, 4, 5))  # 3
print(calculate_statistics("mode", 1, 2, 2, 3, 3, 3))  # [3]