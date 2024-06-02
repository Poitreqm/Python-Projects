# 2248. Intersection of Multiple Arrays
# Given a 2D integer array nums where nums[i] is a non-empty array of distinct positive integers, return the list of integers that are present in each array of nums sorted in ascending order.


nums = [[3, 1, 2, 4, 5], [1, 2, 3, 4], [3, 4, 5, 6]]

s = map(set, nums)

res = set.intersection(*s)

x = []

for i in res:
    x.append(i)
