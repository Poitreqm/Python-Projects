# 2529. Maximum Count of Positive Integer and Negative Integer
# Given an array nums sorted in non-decreasing order, return the maximum between the number of positive integers and the number of negative integers.
# In other words, if the number of positive integers in nums is pos and the number of negative integers is neg, then return the maximum of pos and neg.
# Note that 0 is neither positive nor negative.


nums = [5, 20, 66, 1314]

np = 0
nn = 0
for i in range(len(nums)):
    if nums[i] > 0:
        np += 1
    if nums[i] < 0:
        nn += 1

print(max(np, nn))
