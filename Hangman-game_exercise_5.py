#
# Виселица – продвинутый вариант «угадай число». Игрок должен угадывать буквы в
# загаданном слове. Для упрощенной версии используйте только текст, без графики.
# Потребуется опыт работы со списками, генератор случайных чисел, работа со строками,
# обработка ввода, вывод, цикл while, операторы if/else. Для списка слов
# Для списка слов воспользуйтесь словарем https://github.com/Xethron/Hangman/blob/master/words.txt
#

# файл можно найти в той же папке где и сам скрипт

import random

# import re


def main():
    file_list = open("Words_list_Hangman_game_exercise_5.txt", "r")
    # или "C:\Users\Documents\Projects\Words_list_Hangman_game_exercise_5.txt"

    alphabet_upper = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z"
    # alphabet_lower = "abcdefghijklmnopqrstuvwxyz"
    come_out_letters = ""

    words_list: list[str] = []

    for words in file_list:
        words_list.append(words.strip())  # добавляем все слова из файла в список

    random_word = random.choice(words_list)
    print(random_word)

    print(f"Length: {len(random_word)}")
    print(f"the letters that came out: {come_out_letters}")

    user_letter = input(
        f"""CHOICE A LETTER: {alphabet_upper}: 
"""
    )
    if (
        len(user_letter) != 1
        or user_letter not in alphabet_upper.lower()
        or user_letter == " "
    ):
        print("Pleace choice Letter")
        print(user_letter)
    elif user_letter in random_word and user_letter in alphabet_upper.lower():
        print(user_letter)


if __name__ == "__main__":

    main()
