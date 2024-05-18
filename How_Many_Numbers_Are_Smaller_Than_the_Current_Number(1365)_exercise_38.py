#
# 1365. How Many Numbers Are Smaller Than the Current Number
# Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it.
# That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].
# Return the answer in an array.
#

nums = [6, 5, 4, 8]

arr = [0] * len(nums)

for i in range(len(nums)):
    count = 0
    for j in range(len(nums)):
        if nums[i] > nums[j] and i != j:
            count += 1
        arr[i] = count


print(arr)

