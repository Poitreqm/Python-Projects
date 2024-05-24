# 2441. Largest Positive Integer That Exists With Its Negative
# Given an integer array nums that does not contain any zeros, find the largest positive integer k such that -k also exists in the array.
# Return the positive integer k. If there is no such integer, return -1.


nums = [-10, 8, 6, 7, -2, -3]

ans = []
s = 0

nums.sort(reverse=True)

for i in range(len(nums)):
    if nums[i] * -1 in nums:
        ans.append(nums[i])
        s = max(ans)
        break

    else:
        s = -1


print(s)
