#
# Угадай число – компьютер выберет случайное число, а игроки должны будут по очереди
# угадывать число. При разработке используются: генератор случайных чисел, цикл while,
# условные конструкции if/else, переменные, целые числа и вывод на экран.
#

import random


def guess_number():
    x = random.randint(0, 10)
    print(x)
    while True:  # провекра на число
        try:
            input_number = int(input("I guess the number from 0 to 10: "))
        except ValueError:
            print("Its not a number")
        else:
            while True:  # провекра на число
                try:
                    while input_number != x:
                        input_number = int(input("Incorrect. Try again: "))
                    else:
                        print(f"Good! Number was {input_number}")
                        guess_number()
                except ValueError:
                    print("Its not a number")


guess_number()
