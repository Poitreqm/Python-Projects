#
# Виселица – продвинутый вариант «угадай число». Игрок должен угадывать буквы в
# загаданном слове. Для упрощенной версии используйте только текст, без графики.
# Потребуется опыт работы со списками, генератор случайных чисел, работа со строками,
# обработка ввода, вывод, цикл while, операторы if/else. Для списка слов
# Для списка слов воспользуйтесь словарем https://github.com/Xethron/Hangman/blob/master/words.txt
#

# файл можно найти в той же папке где и сам скрипт

import random


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
            display += display + "_"
    return display


def main():

    word = random_word()
    print(word)
    guessed_letters: list[str] = []

    Life = 5

    while True:
        print("\nWord:", display_word(word, guessed_letters))
        print("Attempts left:", Life)
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You've already guessed that letter.")
        elif guess in word:
            guessed_letters.append(guess)
            if display_word(word, guessed_letters) == word:
                print("\nCongratulations! You guessed the word:", word)
                break
        else:
            guessed_letters.append(guess)
            Life -= 1
            print("Incorrect guess.")

        if Life == 0:
            print("\nYou ran out of attempts. The word was:", word)
            break

    print("Thanks for playing!")

    print("Welcome")


if __name__ == "__main__":

    main()
