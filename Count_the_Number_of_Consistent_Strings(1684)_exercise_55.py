#
# 1684. Count the Number of Consistent Strings
# You are given a string allowed consisting of distinct characters and an array of strings words. A string is consistent if all characters in the string appear in the string allowed.
# Return the number of consistent strings in the array words.
#

import re

allowed = "abc"
words = ["a", "b", "c", "ab", "ac", "bc", "abc"]

count = 0
for i in words:
    if re.fullmatch(
        rf"[{allowed}]*", i
    ):  # ищем только строки с в которых есть эти символы из allowed с помощью регулярной функции
        count += 1
print(count)
