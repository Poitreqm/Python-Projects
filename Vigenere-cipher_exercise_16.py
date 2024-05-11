#
# Шифр Виженера
#

key = "lemon"
# input("Write a key: ")
text = "Attack at down. Me 3-rd world?! KAK DELA BRATAnnn?"
# input("Write a text: ")

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

extended_key = []  # список для того чтобы размножить ключ по длинне текста
key_indexes = []  # индексы ключа для сложения с индексами текста
text_indexes = []  # индексы текста для сложения
sum_indexes = []  # сумма индексов ключа и индексов текста
crypto_text = []  # зашифрованный текст


def get_extended_key():  # растягиваем ключ по длинне текста
    for y in range(len(text)):
        i = y % len(key)
        # берем остаток от деления. Если длинна текса равна 5 а в ключе всего длинна 3 то будет 2. Это значит что берем 2 символа с начала
        extended_key.append(key[i].upper())


def get_index_key():  # добавляем индексы ключа в массив
    for i in extended_key:
        if i in alphabet:
            key_indexes.append(alphabet.index(i))


def get_index_text():  # добавляем индексы в массив
    for y in text:
        if y.upper() not in alphabet:
            text_indexes.append(y)
        elif y.upper() in alphabet:  # проверяем если буква в верхнем регистре
            if y.isupper():  # проверяет является ли i заглавной буквой
                text_indexes.append(alphabet.index(y))
            else:
                text_indexes.append(
                    (alphabet.index(y.upper()))
                )  # Добавляем букву в нижнем регистре


def get_sum_indexes():  # суммируем индексы из текста и ключа
    for x in range(len(key_indexes)):
        if isinstance(text_indexes[x], int):
            if (
                key_indexes[x] + text_indexes[x]
            ) >= 26:  # если больше 26 то нужно вычесть 26 что бы найти буквы в алфавите
                sum_indexes.append(key_indexes[x] + text_indexes[x] - 26)
            else:
                sum_indexes.append(key_indexes[x] + text_indexes[x])
        else:
            sum_indexes.append(
                text_indexes[x]
            )  # просто добавляем символ если он стринговский


def get_crypto_text():
    # проверяем если в тексте есть нижний и верхний регистр и добавляем зашифрованный текст согласно регистру
    for i, y in zip(sum_indexes, text):
        if isinstance(i, int):
            if (
                y.isalpha() and y.islower()
            ):  # Проверяем, является ли символ буквой и находится ли он в нижнем регистре что бы учесть нижний регистр в шифре
                crypto_text.append((alphabet[i]).lower())
            else:
                crypto_text.append(alphabet[i])
        else:
            crypto_text.append(i)

    return "".join(crypto_text)


get_extended_key()  # получаем растянутый ключ по длинне текста
get_index_key()  # получаем индексы ключа
get_index_text()  # получаем индексы текста
get_sum_indexes()  # суммируем индексы ключа и текста

print(f"KEY: {key}")

print(f"TEXT: {text}")

print(
    f"CRYPTY TEXT: {get_crypto_text()}"
)  # находим нужные буквы в алфавите по сумме индексов и выводим их в нужном регистре
