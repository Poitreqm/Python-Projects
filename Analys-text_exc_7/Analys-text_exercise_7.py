#
# Text analysis:
# Write a program that analyzes a text file and outputs various statistics,
# such as the number of words, the number of sentences, the most common characters, etc.
#

from collections import Counter
import re


def most_common_words(text: str, n: int):
    # Приведение текста к нижнему регистру и удаление лишних символов
    text = re.sub(r"[^\w\s]", "", text.lower())
    # Разбивка текста на слова
    words = text.split()
    # Подсчет количества вхождений каждого слова
    word_count = Counter(words)
    # Вывод n самых распространенных слов
    return word_count.most_common(n)


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
counter_variable = Counter(string_variable).most_common(6)
top_words = most_common_words(string_variable, 5)

print(" ")

for character, count in counter_variable:
    if character == " ":  # Most popular symbols exept space
        total_symbols_without_space += count
        continue
    print(f"Most popular symbols: {character}     Count: {count}")

for line in words_list:
    lines += 1
    words += len(line.split())
    total_symbols += len(line)
print("")
for word, count in top_words:
    print(f"Most popular word: {word}     Count: {count}")
print("")
print("Lines:", lines)
print("Words:", words)
print("Total Symbols:", total_symbols)
print("Symbols Without space:", total_symbols - total_symbols_without_space)
print("")
