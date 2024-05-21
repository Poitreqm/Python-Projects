#
# 2176. Count Equal and Divisible Pairs in an Array
# Given a 0-indexed integer array nums of length n and an integer k, return the number of pairs (i, j) where 0 <= i < j < n, such that nums[i] == nums[j] and (i * j) is divisible by k.
#


nums = [3, 1, 2, 2, 2, 1, 3]
k = 2

arr = []

for i in range(len(nums) - 1):
    for j in range(i + 1, len(nums)):
        if nums[i] == nums[j]:
            if (i * j) % k == 0:
                arr.append((i, j))


print(len(arr))
