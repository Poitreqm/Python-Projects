#
# 1480. Running Sum of 1d Array
# Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
# Return the running sum of nums.
#

nums = [3, 1, 2, 10, 1]

arr = [0] * len(nums)

for i in range(0, len(nums)):
    arr[i] = sum(nums[:i]) + nums[i]

print(arr)
