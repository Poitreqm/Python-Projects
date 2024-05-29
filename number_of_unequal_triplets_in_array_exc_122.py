# 2475. Number of Unequal Triplets in Array
# You are given a 0-indexed array of positive integers nums. Find the number of triplets (i, j, k) that meet the following conditions:
# 0 <= i < j < k < nums.length
# nums[i], nums[j], and nums[k] are pairwise distinct.
# In other words, nums[i] != nums[j], nums[i] != nums[k], and nums[j] != nums[k].
# Return the number of triplets that meet the conditions.


nums = [4, 4, 2, 4, 3]

count = 0
for i in range(len(nums)):
    for j in range(i, len(nums)):
        for k in range(j, len(nums)):
            if nums[i] != nums[j] and nums[i] != nums[k] and nums[j] != nums[k]:
                count = count + 1

print(count)
