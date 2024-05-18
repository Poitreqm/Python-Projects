#
# 2824. Count Pairs Whose Sum is Less than Target
# Given a 0-indexed integer array nums of length n and an integer target,
# return the number of pairs (i, j) where 0 <= i < j < n and nums[i] + nums[j] < target.
#


nums = [-6, 2, 5, -2, -7, -1, 3]
target = -2

count = 0
for i in range(0, len(nums) - 1):
    for j in range(i + 1, len(nums)):

        if nums[i] + nums[j] < target:
            count += 1

print(count)
