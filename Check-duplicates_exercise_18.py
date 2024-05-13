#
# Напишите программу, которая берет список и проверяет, повторяется ли любой из его элементов более одного раза. Входные данные воспринимайте как параметры командной строки.
#

while True:
    count = 0
    input_list = []
    dublicates = {}

    try:
        length = int(input("Write length of list: "))
    except ValueError:
        print("Write a number please.")
    else:
        while count < length:
            input_list.append(input("Write element: "))
            count += 1

    for i in input_list:
        result_count = input_list.count(i)  # проверяем сколько повторений
        if result_count > 1:
            # проверяем если в результат больше 1 так как 1 повторение есть у каждого числа
            dublicates[i] = result_count
            # добавляем key как элемент а value как количество повторений

    if len(dublicates) == 0:
        print("No dublicates")
    else:
        for key, value in dublicates.items():
            print(f"Element:  {key}  has  {value} repetitions in the list")
