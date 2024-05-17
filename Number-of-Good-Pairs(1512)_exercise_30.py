#
# Given an array of integers nums, return the number of good pairs.
# A pair (i, j) is called good if nums[i] == nums[j] and i < j.
#

nums = [1, 2, 3, 1, 1, 3]
dictionary = {}
a = []


def numIdenticalPairs(nums: list[int]):
    count = 0
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)): # i + 1гарантирует что i < j
            if nums[i] == nums[j]:
                count += 1
    return count # count будет содержать общее количество хороших пар.


print(numIdenticalPairs(nums))
