#
# Виселица – продвинутый вариант «угадай число». Игрок должен угадывать буквы в
# загаданном слове. Для упрощенной версии используйте только текст, без графики.
# Потребуется опыт работы со списками, генератор случайных чисел, работа со строками,
# обработка ввода, вывод, цикл while, операторы if/else. Для списка слов
# Для списка слов воспользуйтесь словарем https://github.com/Xethron/Hangman/blob/master/words.txt
#

# файл можно найти в той же папке где и сам скрипт

import random
import string


def random_word():
    file_list = open("Words_list_Hangman_game_exercise_5.txt", "r")
    words_list: list[str] = []

    for words in file_list:
        words_list.append(words.strip())  # добавляем все слова из файла в список

    return random.choice(words_list)


def display_word(word: str, guessed_letters: list[str]):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display


def main():
    print("Welcome")
    alphabet = list(string.ascii_lowercase)  # Создание списка букв алфавита
    word = random_word()
    print(word)
    guessed_letters: list[str] = []

    life = 5

    while True:
        print(f"{" ".join(alphabet).upper()}")
        print("Word:", display_word(word, guessed_letters))
        print("Life left:", life)
        guess = input("Guess a letter: ").lower()
        print("")
        if guess not in string.ascii_lowercase:
            print("Guess pleace only one letter")
        elif guess in guessed_letters:
            print("You've already guessed that letter.")
        elif guess in word:
            alphabet.remove(guess)
            guessed_letters.append(guess)
            if display_word(word, guessed_letters) == word:
                print("Congratulations! You guessed the word:", word)
                break
        else:
            guessed_letters.append(guess)
            alphabet.remove(guess)
            life -= 1
            print("Incorrect guess.")

        if life == 0:
            print("You ran out of attempts. The word was:", word)
            break

    print("Thanks for playing!")


if __name__ == "__main__":

    main()
