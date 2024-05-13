#
# Напишите программу, которая берет список из командной строки и делает новый, в котором каждый из элементов первой встречается ровно один раз. Вывод должен быть списком неповторяющихся элементов
#

while True:
    count = 0
    input_list = []
    new_list = []
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
        if i not in new_list:  # проверяем если элемента еще нет в новом списке
            new_list.append(i)

    print(new_list)
