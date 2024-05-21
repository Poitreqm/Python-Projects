#
# 3131. Find the Integer Added to Array I
# You are given two arrays of equal length, nums1 and nums2.
# Each element in nums1 has been increased (or decreased in the case of negative) by an integer, represented by the variable x.
# As a result, nums1 becomes equal to nums2. Two arrays are considered equal when they contain the same integers with the same frequencies.
# Return the integer x.
#

nums1 = [2, 6, 4]
nums2 = [9, 7, 5]

nums1.sort()
nums2.sort()

x = 0

for i in range(len(nums2)):
    x = nums2[i] - nums1[i]

print(x)
