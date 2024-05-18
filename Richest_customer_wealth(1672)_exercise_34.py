#
# 1672. Richest Customer Wealth
# You are given an m x n integer grid accounts where accounts[i][j] is the amount of money the i​​​​​​​​​​​th​​​​ customer has in the j​​​​​​​​​​​th​​​​ bank. Return the wealth that the richest customer has.
# A customer's wealth is the amount of money they have in all their bank accounts. The richest customer is the customer that has the maximum wealth.
#

import numpy as np

accounts = [[1, 2, 3], [3, 2, 1]]

rows, columns = np.shape(accounts)  # узнаем размеры матрицы

r = [0] * rows  # создаем массив из нулей
c = [0] * columns  # создаем массив из нулей


for i in range(rows):
    for j in range(columns):
        r[i] += accounts[i][j]
        c[j] += accounts[i][j]

print(max(r))
