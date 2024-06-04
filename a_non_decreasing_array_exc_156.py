# A non-decreasing array
# An array of integers is given. We need to check whether it is possible to make a non-decreasing array from nums by changing no more than one element.
# Note: A non-decreasing array is an array in which each subsequent element is greater than or equal to the previous one.

nums = [1, 2, 3]

b = False
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] > nums[j]:
            nums[i] = nums[j] - 1


if nums == sorted(nums):
    b = True

print(b)
