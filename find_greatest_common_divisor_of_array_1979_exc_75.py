#
# 1979. Find Greatest Common Divisor of Array
# Given an integer array nums, return the greatest common divisor of the smallest number and largest number in nums.
# The greatest common divisor of two numbers is the largest positive integer that evenly divides both numbers.
#


nums = [7, 5, 6, 8, 3]

a = max(nums)
b = min(nums)

while b != 0:
    temp = b
    b = a % b
    a = temp

print(a)
