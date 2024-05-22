# 1. Two Sum
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

nums = [2, 7, 11, 15]
target = 9

arr = []

for i in range(0, len(nums) - 1):
    for j in range(i + 1, len(nums)):
        if nums[i] + nums[j] == target:
            arr.append(i)
            arr.append(j)

print(arr)
