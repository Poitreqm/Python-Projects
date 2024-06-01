2643. Row With Maximum Ones
Given a m x n binary matrix mat, find the 0-indexed position of the row that contains the maximum count of ones, and the number of ones in that row.
In case there are multiple rows that have the maximum count of ones, the row with the smallest row number should be selected.
Return an array containing the index of the row, and the number of ones in it.


mat = [[0, 1], [1, 0]]

arr = {}

for i in mat:
    arr[mat.index(i)] = i.count(1)


if min(arr.values()) == max(arr.values()):
    print([min(arr.keys()), max(arr.values())])
else:
    key = max(arr, key=arr.get)
    print([key, max(arr.values())])
