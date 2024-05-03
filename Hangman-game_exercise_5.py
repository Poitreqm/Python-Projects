#
# Виселица – продвинутый вариант «угадай число». Игрок должен угадывать буквы в
# загаданном слове. Для упрощенной версии используйте только текст, без графики.
# Потребуется опыт работы со списками, генератор случайных чисел, работа со строками,
# обработка ввода, вывод, цикл while, операторы if/else. Для списка слов
# Для списка слов воспользуйтесь словарем https://github.com/Xethron/Hangman/blob/master/words.txt
#

# файл можно найти в той же папке где и сам скрипт

import random
import re


def replacer(s: str, newstring: str, index: int, nofail: bool = False, count: int = 0):
    
    if not nofail and index not in range(len(s)):
        raise ValueError("index outside given string")

    # if not erroring, but the index is still not in the correct range..
    if index < 0:  # add it to the beginning
        return newstring + s
    if index > len(s):  # add it to the end
        return s + newstring

    # insert the new string between "slices" of the original
    return s[:index] + newstring + s[index + 1 :].replace(s, newstring, count)


# [a-zA-Z]


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

    replaced_word = re.sub(pattern=r"\w", string=random_word, repl="_", count=0)  # заменить все буквы на _
    
    print(random_word)

    print(f"Length: {len(random_word)}")
    print(f"WORD: {replaced_word}")
    while True:
        user_letter = input(
            f"""CHOICE A LETTER: {alphabet_upper}: 
""")
        if (len(user_letter) != 1 or user_letter.lower() not in alphabet_upper.lower() or user_letter == " "):
            
            print("Pleace choice a Letter")

        elif (user_letter.lower() in random_word and user_letter in alphabet_upper.lower()):
            
            print(f"ALL: {re.search(user_letter, random_word)}")
            y = replacer(replaced_word, user_letter.lower(), list(random_word).index(user_letter), False, 2)
            
            print(y.upper())
            come_out_letters = user_letter.lower()
            g = alphabet_upper.replace(f" {user_letter.upper()}", "")
            
            replaced_word = re.sub(pattern=r"\w", string=random_word, repl="_", count=0)
            
            user_letter = input(f"""CHOICE A LETTER: {g}: """)
            
            print(come_out_letters)


if __name__ == "__main__":

    main()
