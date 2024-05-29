# 1636. Sort Array by Increasing Frequency
# Given an array of integers nums, sort the array in increasing order based on the frequency of the values. If multiple values have the same frequency, sort them in decreasing order.
# Return the sorted array.


nums = [2, 3, 1, 3, 2]


for i in range(len(nums)):
    for j in range(len(nums)):
        if nums.count(nums[i]) < nums.count(nums[j]):
            tmp = nums[i]
            nums[i] = nums[j]
            nums[j] = tmp
        elif nums.count(nums[i]) == nums.count(nums[j]):
            if nums[i] > nums[j]:
                tmp = nums[i]
                nums[i] = nums[j]
                nums[j] = tmp

print(nums)
