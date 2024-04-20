# -*- coding: utf-8 -*-
"""
Stwórz listę tupli, gdzie każda tupla zawiera informacje o produkcie: nazwę, cenę i kategorię. 
#Przykład
products = [
    ("Laptop", 1500, "Elektronika"),
    ("Kubek", 10, "Dom"),
    ("Słuchawki", 100, "Elektronika"),
    ("Sok", 5, "Żywność"),
    ("Telefon", 2000, "Elektronika"),
    ("Długopis", 2, "Biuro"),
    ("Papier", 10, Biuro),
    ("Koszulka", 20, "Moda"),
    ("Pomarańcza", 5,"Żywność")
]

1. Utwórz set zawierający wszystkie unikalne kategorie produktów.
2. Oblicz średnią cenę produktów oraz średnią cenę produktów z danej kategorii.
3. Znajdź najdroższy i najtańszy produkt oraz najdroższy i najtańszy produkt z danej kategorii.
4. Stwórz listę zawierającą nazwy wszystkich produktów o cenie powyżej 100 zł.
5. Wypisz informacje o produktach, których kategoria zaczyna się od litery "E".
"""


def averagePrice(products):
    prices_sum = 0
    for product in products:
        prices_sum += product[1]
    return prices_sum / len(products)


products = [
    ("Laptop", 1500, "Elektronika"),
    ("Kubek", 10, "Dom"),
    ("Słuchawki", 100, "Elektronika"),
    ("Sok", 5, "Żywność"),
    ("Telefon", 2000, "Elektronika"),
    ("Długopis", 2, "Biuro"),
    ("Papier", 10, "Biuro"),
    ("Koszulka", 20, "Moda"),
    ("Pomarańcza", 5, "Żywność")
]
categories = set()
for product in products:
    categories.add(product[2])
print("Average price:", averagePrice(products))
category = list(categories)[0]
products_in_category = list()
for product in products:
    if product[2] == category:
        products_in_category.append(product)
print(f"Average price in category '{category}': ", averagePrice(products_in_category))
