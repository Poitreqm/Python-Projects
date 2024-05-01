#
# Генератор паролей – простое приложение, генерирующее случайный пароль. Из навыков
# потребуется генератор случайных чисел, работа со строками, числами, вывод на экран,
# последовательности.
#

import random

alphabet_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alphabet_lower = "abcdefghijklmnopqrstuvwxyz"
numbers = "0123456789"
symbols = "!@#$%^&*()_+-=[]{}|;:,.<>?"

random_choice_alphabet_upper = random.choice(alphabet_upper)
random_choice_alphabet_lower = random.choice(alphabet_lower)
random_choice_numbers = random.choice(numbers)
random_choice_symbols = random.choice(symbols)

generated_password: list[str] = []

# Длина: 12 символов.
# Разнообразие: Включает заглавные буквы, строчные буквы, цифры и специальные символы.
# Уникальность: Не использует легко угадываемые пароли или очевидные последовательности.

for i in range(3):
    generated_password.append(random.choice(alphabet_upper))
    generated_password.append(random.choice(alphabet_lower))
    generated_password.append(random.choice(numbers))
    generated_password.append(random.choice(symbols))


string_password = "".join(generated_password)  # преобразовываем списокь в строку

print(f"Length:     {len(string_password)}")
print(f"Password:   {string_password}")
