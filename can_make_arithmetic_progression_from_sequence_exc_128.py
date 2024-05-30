# 1502. Can Make Arithmetic Progression From Sequence
# A sequence of numbers is called an arithmetic progression if the difference between any two consecutive elements is the same.
# Given an array of numbers arr, return true if the array can be rearranged to form an arithmetic progression. Otherwise, return false.


arr = [1, 2, 4]

arr.sort(reverse=True)

b = False
res = set()

for i in range(len(arr) - 1):
    tmp = arr[i] - arr[i + 1]
    res.add(tmp)

print(res)

if len(res) == 1:
    b = True

print(b)
