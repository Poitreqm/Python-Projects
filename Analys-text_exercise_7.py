#
# Анализ текста:
# Напишите программу, которая анализирует текстовый файл и выводит различные статистики,
# такие как количество слов, количество предложений, наиболее часто встречающиеся символы и т. д.
#

from collections import Counter

file_list = open("Text_list_Analys_text_exercise_7.txt", "r")
words_list: list[str] = []

for words in file_list:
    words_list.append(words.strip())

print(words_list)

string_variable = "".join(words_list)


lines = 0
words = 0
total_symbols = 0
total_symbols_without_space: int = 0
counter_variable = Counter(string_variable).most_common(5)

print(" ")

for key, value in counter_variable:
    if key == " ":
        total_symbols_without_space += value
        continue
    print(f"Most popular symbols(exept space): {key} Count: {value}")

for line in words_list:
    lines += 1
    words += len(line.split())
    total_symbols += len(line)


print("Lines:", lines)
print("Words:", words)
print("Total Symbols:", total_symbols)
print("Symbols Without space:", total_symbols - total_symbols_without_space)
