#
# Симулятор игры в кости – понадобится генератор случайных чисел, который будет
# генерировать случайные числа от 1 до 6, цикл while и вывод на экран для уточнения
# нужно ли сделать новый бросок, обработка ввода и цикл if/else для обработки
# введенного игроком значения.
#

import random


def random_choice():
    random_number = random.choice(range(1, 6))
    print(f"Fell out: {random_number}")
    return random_number


while True:
    again = input("Start game? Write y/n: ")
    if again.lower() == "y":
        random_choice()
    elif again.lower() == "n":
        print("Good buy. Thx for game.")
        break
    else:
        print("I dont undestand. Write y or n")
        continue
