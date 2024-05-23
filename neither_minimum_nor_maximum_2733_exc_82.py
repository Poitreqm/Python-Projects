#
# 2733. Neither Minimum nor Maximum
# Given an integer array nums containing distinct positive integers, find and return any number from the array that is neither the minimum nor the maximum value in the array, or -1 if there is no such number.
# Return the selected integer.
#

nums = [3, 2, 1, 4]

result = -1
for i in nums:
    if i != min(nums) and i != max(nums) and len(nums) > 2:
        print(i)
        result = i
