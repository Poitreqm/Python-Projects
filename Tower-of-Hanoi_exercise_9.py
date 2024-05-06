#
# Ханойская башня - три стержня, на один из которых нанизаны восемь колец, причём кольца отличаются размером и лежат меньшее на большем.
# Задача состоит в том, чтобы перенести пирамиду из восьми колец за наименьшее число ходов на другой стержень.
# За один раз разрешается переносить только одно кольцо, причём нельзя класть большее кольцо на меньшее.
#

# глбобальная переменная


def move_disk(disk: int, first: str, second: str, third: str):
    global steps_count
    if disk == 1:
        print(f"Move disk from {first} to {second}")
        steps_count += 1
    else:
        move_disk(disk - 1, first, third, second)
        print(f"Move disk from {first} to {second}")
        move_disk(disk - 1, third, second, first)
        steps_count += 1


numbers_disks = 3
steps_count = 0
move_disk(numbers_disks, "A", "C", "B")
print(f"Total steps: {steps_count}")
