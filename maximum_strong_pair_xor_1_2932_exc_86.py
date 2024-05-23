#
# 2932. Maximum Strong Pair XOR I
# You are given a 0-indexed integer array nums. A pair of integers x and y is called a strong pair if it satisfies the condition:
# |x - y| <= min(x, y)
# You need to select two integers from nums such that they form a strong pair and their bitwise XOR is the maximum among all strong pairs in the array.
# Return the maximum XOR value out of all possible strong pairs in the array nums.
# Note that you can pick the same integer twice to form a pair.
#

nums = [5, 6, 25, 30]

arr = []

for i in range(0, len(nums)):
    for j in range(i, len(nums)):
        if abs(nums[i] - nums[j]) <= min(nums[i], nums[j]):
            tmp = nums[i] ^ nums[j]
            arr.append(tmp)

print(max(arr))
