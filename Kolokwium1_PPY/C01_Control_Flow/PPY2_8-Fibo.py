# napisz kod, który wyświetli ciąg fibonnaciego do 10 miejsc (https://pl.wikipedia.org/wiki/Ci%C4%85g_Fibonacciego)
# pierwsze dwie liczby w ciągu
def fiboFunction(amount_of_fibonacci_numbers):
    fibonacci_numbers = [0, 1]
    for i in range(2, amount_of_fibonacci_numbers):
        fibonacci_numbers.append((fibonacci_numbers[i - 2] + fibonacci_numbers[i - 1]))
    return fibonacci_numbers


print("Ciąg Fibonacciego:")
print(fiboFunction(50))
