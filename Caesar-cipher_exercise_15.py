#
# Алгоритма шифрования Цезаря на python. Программа принимает в качестве входных параметров из командной строки текст и ключ и выводит зашифрованный текст в консоль
#

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

while True: 
    crypto_list: list[str] = [] # список куда добавляем наши новые буквы 
    # вставляем наш массив в whiel что бы каждый раз создавался новый

    try: 
        key = int(input("Key=: ")) 
    except ValueError:
        print("Key may to be only one number")
    if key > 26:
        print("If the key is 0 or 26 or greater than 26, text will not be encrypted since there are only 26 letters in the alphabet.") # если ключ больше 26 то шифровка не имеет смысла
        print("Key 0 or 26 or > 26 will not change the shift")
    else: 
        text = input("Write a text: ")

        substring = alphabet[key:] + alphabet[:key] # берем символы и добавляем те что отсекаем в конец тем самым создавая

        for i in text:
            if i.upper() not in substring: # проверяем если это пробел, цифра или символ
                crypto_list.append(i)
            elif i.upper() in substring: # проверяем если буква в верхнем регистре
                if i.isupper(): # проверяет является ли i заглавной буквой
                    crypto_list.append(substring[alphabet.index(i)])
                else:
                    crypto_list.append(substring[alphabet.index(i.upper())].lower()) # Добавляем букву в нижнем регистре

        print(f"KEY:              {key}")
        print(f"YOUR TEXT:        {text}")
        print(f"CAESAR CIPHER:    {"".join(crypto_list)}")
        
