# 2057. Smallest Index With Equal Value
# Given a 0-indexed integer array nums, return the smallest index i of nums such that i mod 10 == nums[i], or -1 if such index does not exist.
# x mod y denotes the remainder when x is divided by y.


nums = [7, 8, 3, 5, 2, 6, 3, 1, 1, 4, 5, 4, 8, 7, 2, 0, 9, 9, 0, 5, 7, 1, 6]

arr = []

s = 0
for i in range(len(nums)):
    if (i % 10) == (nums[i]):
        arr.append(i)

print(arr)

if len(arr) != 0:
    s = min(arr)
else:
    s = -1

print(s)
