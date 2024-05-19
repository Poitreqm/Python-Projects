#
# 2574. Left and Right Sum Differences
# Given a 0-indexed integer array nums, find a 0-indexed integer array answer where:
# answer.length == nums.length.
# answer[i] = |leftSum[i] - rightSum[i]|.
# Where:
# leftSum[i] is the sum of elements to the left of the index i in the array nums. If there is no such element, leftSum[i] = 0.
# rightSum[i] is the sum of elements to the right of the index i in the array nums. If there is no such element, rightSum[i] = 0.
# Return the array answer.
#

nums = [10, 4, 8, 3]

left_sum = [0] * len(nums)
right_sum = [0] * len(nums)

sum_arr = [0] * len(nums)

right_sum[0] = 0

for i in range(len(nums)):
    left_sum[i] = sum(nums[:i])

for j in reversed(range(len(nums))):
    right_sum[j] = sum(nums[j + 1 :])

for y in range(len(sum_arr)):
    sum_arr[y] = abs(left_sum[y] - right_sum[y])

print(left_sum)
print(right_sum)
print(sum_arr)
