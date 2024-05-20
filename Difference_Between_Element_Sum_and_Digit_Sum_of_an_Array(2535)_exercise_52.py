#
# 2535. Difference Between Element Sum and Digit Sum of an Array
# You are given a positive integer array nums.
# The element sum is the sum of all the elements in nums.
# The digit sum is the sum of all the digits (not necessarily distinct) that appear in nums.
# Return the absolute difference between the element sum and digit sum of nums.
# Note that the absolute difference between two integers x and y is defined as |x - y|.
#

nums = [1, 15, 6, 3]

element_sum = 0
digit_sum = 0
difference = 0

for i in range(len(nums)):
    element_sum += nums[i]
    if len(str(nums[i])) > 1:
        for y in range(len(str(nums[i]))):
            digit_sum += int(str(nums[i])[y])
    else:
        digit_sum += nums[i]

difference = element_sum - digit_sum

print(element_sum)
print(digit_sum)
print(difference)
