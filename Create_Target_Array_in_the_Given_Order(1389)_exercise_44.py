#
# 1389. Create Target Array in the Given Order
# Given two arrays of integers nums and index. Your task is to create target array under the following rules:
# Initially target array is empty.
# From left to right read nums[i] and index[i], insert at index index[i] the value nums[i] in target array.
# Repeat the previous step until there are no elements to read in nums and index.
# Return the target array.
# It is guaranteed that the insertion operations will be valid.
#

nums = [0, 1, 2, 3, 4]
index = [0, 1, 2, 2, 1]

target = []

for num, idx in zip(nums, index):
    target.insert(idx, num)

print(target)
