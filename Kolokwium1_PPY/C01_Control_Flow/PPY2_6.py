# oblicz silnię podanej liczby
def factorialFunction(number):
    result = 1
    for i in range(1, number + 1):
        result *= i
    return result


num = 10
print(factorialFunction(num))
