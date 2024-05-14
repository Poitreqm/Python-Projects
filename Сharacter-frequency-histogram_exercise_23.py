#
# Реализовать программу на Python для создания гистограммы частоты встречаемости символов в заданном тексте.
# Программа должна принять текст в качестве входного параметра и вывести в консоль содержимое словаря,
# содержащего ключи — символы из текста, и значения — количество вхождений соответствующего символа.
#

text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."

list_text = []

dictionary = {}

# text = text.replace(" ", "").lower()
# # убираем все пробелы из текста если потребуется

list_text = list(text)  # преобразовываем текст в список одним ловким движением :)

for i in list_text:
    result = list_text.count(i)  # ищем как часто в тексте прсокакивает искомый элемент
    dictionary[i] = result  # добавляем в ключ элемент и в результат его частоту
    print(result)

for key, value in dictionary.items():
    # вывод списка элементов и количества повторения
    print(f"Character: {key}  - {value} repeats")
