#
# Напишите программу, которая берет список и проверяет, повторяется ли любой из его элементов более одного раза. Входные данные воспринимайте как параметры командной строки.
#

while True:
    count = 0
    input_list = []
    repeat = {}

    try:
        length = int(input("Write length of list: "))
    except ValueError:
        print("Write a number please.")
    else:
        while count < length:
            input_list.append(input("Write element: "))
            count += 1

    # array = [2, 4, 6, 0, "false", "true", 2, 0, 144, "false", ".", "."]

    for i in input_list:
        result = input_list.count(i)  # проверяем сколько повторений
        if result > 1:
            # проверяем если в результат больше 1 так как 1 повторение есть у каждого числа
            repeat[i] = (
                result  # добавляем key как элемент а value как количество повторений
            )

    for key, value in repeat.items():
        print(f"Element:  {key}  have  {value} repeats")
