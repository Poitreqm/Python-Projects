#
# 1351. Count Negative Numbers in a Sorted Matrix
# Given a m x n matrix grid which is sorted in non-increasing order both row-wise and column-wise, return the number of negative numbers in grid.
#

grid = [[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]]

count = 0

for i in grid:
    for y in i:
        if y < 0:
            count = count + 1

print(count)
