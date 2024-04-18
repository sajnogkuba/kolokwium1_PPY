"""
A. 
napisz program, którego wynik będzie jak poniżej
Podpowiedź: argumenty, które przyjmuje funkcja range to (start, stop, step)
step przyjmuje domyślnie wartość 1
5 4 3 2 1 
4 3 2 1 
3 2 1 
2 1 
1 
"""


def functionA(number):
    number = int(number)
    for i in range(number):
        for j in range(number - i, 0, -1):
            print(j, end=' ')
        print()


functionA(10)

"""
B. 
Rozszerz powyższy kod o warunki i dostosuj go do poniższego wzoru:
11 # 9 -8 7 -6 # -4 3 -2 1 
# 9 -8 7 -6 # -4 3 -2 1 
9 -8 7 -6 # -4 3 -2 1 
-8 7 -6 # -4 3 -2 1 
7 -6 # -4 3 -2 1 
-6 # -4 3 -2 1 
# -4 3 -2 1 
-4 3 -2 1 
3 -2 1 
-2 1 
1 
"""
print()
print()
print()


def functionB(number):
    number = int(number)
    for i in range(number):
        for j in range(number - i, 0, -1):
            if j % 5 == 0:
                print("#", end=' ')
            elif j % 2 == 0:
                print(-j, end=' ')
            else:
                print(j, end=' ')
        print()


functionB(11)
