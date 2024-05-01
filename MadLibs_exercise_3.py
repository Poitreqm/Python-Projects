#
# Генератор MadLibs - игра, в которой в пробелы нужно вставлять глупые слова, a после
# зачитывать. Для реализации понадобится понимание строк, переменных, конкатенация,
# ввод данных и вывод.
#
import time
import random
import re

text_one = """
On the vast [place],
Strolled [name].
He/She found [object],
And encountered [animal].
"""

text_two = """
On the [adjective] road,
Drove [name].
He/She found [object],
And met [animal].
"""

text_three = """
Together they [verb] [adverb],
And [name] exclaimed, "[phrase]!"
[Animal] said, "[phrase]!",
And [object] did, "[phrase]!".
"""

text_four = """
Together they [verb] [adverb],
And [name] exclaimed, "[phrase]!"
[Animal] said, "[phrase]!",
And [object] did, "[phrase]!".
"""


def welcome_text():
    print(
        """ 
Madlibs - is a word-based game where players fill in blanks in a story with various types of words (nouns, verbs, adjectives, etc.),
          """
    )


def main():
    current_text_game = random.choice(
        [text_one, text_two, text_three, text_four]
    )  # выбирает случайный текст

    for i in current_text_game:
        time.sleep(0.04)  # симулируем напечатанный текст
        print(i, end="", flush=True)

    new_word: list[str] = []
    old_words: list[str] = []
    pattern = r"\[(.*?)\]"

    match = re.findall(pattern=pattern, string=current_text_game)
    # находим все по паттерну Этот паттерн позволяет искать все между [""]

    print("")  # создаем пустую строку для лучшей читаемости
    for x in match:
        user_input_words = input(f"Add the {x}: ")
        old_words.append(x)
        new_word.append(user_input_words)

    for j in range(len(new_word)):
        current_text_game = current_text_game.replace(f"[{old_words[j]}]", new_word[j])
    # ищем старые слова и заменяем их новыми

    print(current_text_game)


if __name__ == "__main__":
    welcome_text()
    while True:  # зацикливаем игру
        main()
