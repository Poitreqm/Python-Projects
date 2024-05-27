# 1403. Minimum Subsequence in Non-Increasing Order
# Given the array nums, obtain a subsequence of the array whose sum of elements is strictly greater than the sum of the non included elements in such subsequence.
# If there are multiple solutions, return the subsequence with minimum size and if there still exist multiple solutions, return the subsequence with the maximum total sum of all its elements. A subsequence of an array can be obtained by erasing some (possibly zero) elements from the array.
# Note that the solution with the given constraints is guaranteed to be unique. Also return the answer sorted in non-increasing order.


nums = [4, 3, 10, 9, 8]

nums.sort(reverse=True)
arr = []

s = 0

print(nums)

for i in range(len(nums)):

    if s <= sum(nums) - s:
        arr.append(nums[i])
        s = sum(arr)
    else:
        break

print(arr)
