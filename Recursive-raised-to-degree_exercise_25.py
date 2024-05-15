#
# Создайте рекурсивную функцию, которая при заданном числе и степени возвращает число, возведенное в степень
#


def func(a, b):
    if b == 0:
        return 1
    elif b == 1:
        return a
    elif b < 0:
        return 1 / func(a, -b)
    else:
        return a * func(a, b - 1)


print(func(2, -10))
