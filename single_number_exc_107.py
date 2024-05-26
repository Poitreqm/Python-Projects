136. Single Number
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
You must implement a solution with a linear runtime complexity and use only constant extra space.


nums = [2, 2, 1]

num = 0

for i in nums:
    if nums.count(i) == 1:
        num = i

print(num)
