def countDigitsStr(number):
    return len(str(number))


def countDigits(number):
    digits = 0
    while number > 0:
        digits += 1
        number = number // 10
    return digits


# 3A.
# Napisz program, który policzy ile jest cyfr w liczbie, przy pomocy funckji len()
print(countDigitsStr(123456))

# 3B.
# Napisz program, który policzy ile jest cyfr w tej samej liczbie innym sposobem
# pomyśl o szybkości obliczeń
print(countDigits(123456))
