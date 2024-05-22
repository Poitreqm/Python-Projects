#
# 1295. Find Numbers with Even Number of Digits
# Given an array nums of integers, return how many of them contain an even number of digits.
#


nums = [12, 345, 2, 6, 7896]

count = 0

for i in range(len(nums)):
    if len(str(nums[i])) % 2 == 0:
        count = count + 1
print(count)
