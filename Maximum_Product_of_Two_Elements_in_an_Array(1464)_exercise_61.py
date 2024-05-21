#
# 1464. Maximum Product of Two Elements in an Array
# Given the array of integers nums, you will choose two different indices i and j of that array. Return the maximum value of (nums[i]-1)*(nums[j]-1).
#

nums = [3, 7]


arr = []

for i in range(0, len(nums) - 1):
    for y in range(i + 1, len(nums)):
        arr.append((nums[i] - 1) * (nums[y] - 1))
        print((nums[i] - 1) * (nums[y] - 1))

print(max(arr))
