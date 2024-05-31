# 1572. Matrix Diagonal Sum
# Given a square matrix mat, return the sum of the matrix diagonals.
# Only include the sum of all the elements on the primary diagonal and all the elements on the secondary diagonal that are not part of the primary diagonal.


import numpy as np


mat = [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]

mat = np.array(mat)  # исспользуем нумпай для нашей матрицы

n = mat.shape[0]  # узнаем размер

sum_result = 0
r = np.trace(mat)
x = np.trace(np.fliplr(mat))  # меняем ось с помощью fliplr

sum_result = r + x
if (
    n % 2 == 1
):  # узнаем если массив нечетный и вычитаем элемент который повторяется дважды для обоих диагоналей
    middle = mat[n // 2, n // 2]  # находим центральный элемент
    sum_result = sum_result - middle

print(sum_result)
