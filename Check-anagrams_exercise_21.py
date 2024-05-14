#
# Напишите программу, которая проверяет, являются ли две символические строки анаграммами.
# Два слова-это анаграммы, если мы можем переставить буквы одного, чтобы написать другое.
# "Vladimir Nabokov" = "Vivian Darkbloom" "rocket boys" = "october sky"
# Результат, который должен быть выведен, - это строка True, если в противном случае слова не являются анаграммами - False.
#

a = "vladimir nabokov"
b = "vivian darkbloom"


def are_anagrams(str1, str2):
    # Удаляем пробелы и приводим все символы к нижнему регистру для более точного сравнения
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    # Сортируем символы в обеих строках и сравниваем их
    return sorted(str1) == sorted(str2)


print(are_anagrams(a, b))
