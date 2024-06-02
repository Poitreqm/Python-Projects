# This task is taken from Avito Weekend Offer for analysts
# You are given a set of numbers in the form of a Python list. It is necessary to find the median of this numerical series.
# Write the Find Media n function, which will return a single number - the median value.
# The FindMedian function accepts an arr input - an initial list with numbers.

arr = [1, 5, 2, 3, 6]

arr.sort()

res = 0

if len(arr) != 0:
    if len(arr) % 2 == 0:
        idx = len(arr) // 2
        res = (arr[idx] + arr[idx - 1]) / 2
    else:
        idx = len(arr) / 2
        res = arr[int(idx)]
else:
    res = None

print(res)
