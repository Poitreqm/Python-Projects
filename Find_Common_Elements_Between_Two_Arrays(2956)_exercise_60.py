#
# 2956. Find Common Elements Between Two Arrays
# You are given two 0-indexed integer arrays nums1 and nums2 of sizes n and m, respectively.
# Consider calculating the following values:
# The number of indices i such that 0 <= i < n and nums1[i] occurs at least once in nums2.
# The number of indices i such that 0 <= i < m and nums2[i] occurs at least once in nums1.
# Return an integer array answer of size 2 containing the two values in the above order.
#

nums1 = [10, 30, 16, 18]
nums2 = [23, 30, 30, 6, 10, 26, 9, 27, 6, 16, 18, 10, 27, 2, 20, 7, 16]

c1 = 0
c2 = 0

for i in range(0, len(nums1)):
    if nums1[i] in nums2:
        c1 += 1

for i in range(0, len(nums2)):
    if nums2[i] in nums1:
        c2 += 1

print([c1, c2])
