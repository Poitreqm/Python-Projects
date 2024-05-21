#
# 3005. Count Elements With Maximum Frequency
# You are given an array nums consisting of positive integers.
# Return the total frequencies of elements in nums such that those elements all have the maximum frequency.
# The frequency of an element is the number of occurrences of that element in the array.
#

nums = [1, 2, 2, 3, 1, 4]

d = {}

count = 0

for i in range(len(nums)):
    d[nums[i]] = nums.count(nums[i])


for i, j in d.items():
    if max(d.values()) == j:
        count = count + j

print(count)
