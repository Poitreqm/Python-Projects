#
# Камень, ножницы, бумага - мини-игра, в которую можно играть в одиночку
# с компьютером. При разработке потребуются знания генератора случайных чисел, вывод
# на экран, обработка ввода, цикл while и оператор if/else.
#

import random

print("Welcome to the game rock paper scissors. Pleace write your choise")
print(
    """
      rock
      paper
      scrissors
      """
)
print("Good luck")


game_list = ["rock", "paper", "scrissors"]


while True:
    user_choice = input("Write your choice: ")

    if user_choice == "rock" or user_choice == "paper" or user_choice == "scrissors":
        computer_random_choice = random.choice(game_list)
        print(computer_random_choice)
        if computer_random_choice == user_choice:
            print(f"{computer_random_choice} vs {computer_random_choice}. Drawn game.")
        elif computer_random_choice == "rock" and user_choice == "paper":
            print("Paper vs Rock. You win.")
        elif computer_random_choice == "rock" and user_choice == "scrissors":
            print("Scrissors vs Rock. You lose.")
        elif computer_random_choice == "paper" and user_choice == "rock":
            print("Rock vs Paper. You lose.")
        elif computer_random_choice == "paper" and user_choice == "scrissors":
            print("Scrissors vs Paper. You win.")
        elif computer_random_choice == "scrissors" and user_choice == "rock":
            print("Rock vs Scrissors. You win.")
        elif computer_random_choice == "scrissors" and user_choice == "paper":
            print("Paper vs Scrissors. You lose.")
    else:
        print("I dont undestand... Write rock, paper or scrissors")
