#
# Алгоритм двоичного поиска - Пользователю будет предложено ввести число, которое программа будет искать в
# данном списке и выводить соответствующий результат. Во время поиска берется
# среднее значение и сравнивается с искомым. Если значение найдено, то возвращается
# результат об успехе. Если значение меньше, то дальше будет аналогичным образом
# рассматривать левая часть, т. е. та, что меньше среднего значения. В противном случае,
# рассматривается правая часть. И так будет происходить до тех пор, пока значение не
# будет найдено или список не окажется пуст
#

# Алгоритм двоичного поиска не работает в неотсартированном массиве

array = [0, 10, 3, 11, 2, 4, 5, 1, 6, 12, 13, 15, 7, 14, 8, 9]
length_array = len(array)

for i in range(length_array - 1):
    for j in range(0, length_array - i - 1):
        if array[j] > array[j + 1]:
            temp = array[j]
            array[j] = array[j + 1]
            array[j + 1] = temp

print(array)
user_input = input("The array is already pre-sorted. Array is from 0 to 15: ")

start_index = 0
end_index = len(array) - 1


def binary_search(array: list[int], number: int):
    low = 0
    high = len(array) - 1

    while low <= high:
        mid = (low + high) // 2

        if array[mid] == number:
            return mid  # Искомый элемент найден, возвращаем его индекс
        elif array[mid] < number:
            low = mid + 1  # Искомый элемент находится в правой половине массива
        else:
            high = mid - 1  # Искомый элемент находится в левой половине массива

    return -1  # Если целевой элемент не найден


result_index = binary_search(array, int(user_input))

if result_index != -1:
    print(f"Number {user_input} finded. Index is {result_index}.")
else:
    print(f"Number {user_input} is not in array")
