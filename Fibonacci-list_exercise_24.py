#
# Создайте рекурсивную функцию для вычисления первых n чисел Фибоначчи и их хранения в списке.
# Реализация должна хранить уже рассчитанные значения,
# чтобы при рекурсивном вызове с уже рассчитанным аргументом значение принималось напрямую, а не вычислялось.
#

n = 10


def fibonacci(n, dictionary=None):
    if dictionary is None:
        dictionary = {}

    if n in dictionary:
        return dictionary[n]

    if n <= 1:
        dictionary[n] = n
    else:
        return fibonacci(n - 1, dictionary) + fibonacci(n - 2, dictionary)

    return dictionary[n]


for i in range(n):
    print(fibonacci(i, {}))
