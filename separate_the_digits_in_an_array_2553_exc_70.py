#
# 2553. Separate the Digits in an Array
# Given an array of positive integers nums, return an array answer that consists of the digits of each integer in nums after separating them in the same order they appear in nums.
# To separate the digits of an integer is to get all the digits it has in the same order.
# For example, for the integer 10921, the separation of its digits is [1,0,9,2,1].
#

nums = [13, 25, 83, 77]

s = ""

arr = []
for i in range(len(nums)):
    s += str(nums[i])

for i in range(len(s)):
    arr.append(int(s[i]))

print(arr)
