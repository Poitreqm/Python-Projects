#
# 2215. Find the Difference of Two Arrays
# Given two 0-indexed integer arrays nums1 and nums2, return a list answer of size 2 where:
# answer[0] is a list of all distinct integers in nums1 which are not present in nums2.
# answer[1] is a list of all distinct integers in nums2 which are not present in nums1.
# Note that the integers in the lists may be returned in any order.
#


nums1 = [1, 2, 3, 3]
nums2 = [1, 1, 2, 2]

arr = []

count_1 = 0
count_2 = 0

for i in range(len(nums1)):
    if nums1[i] not in nums2 and nums1[i] not in arr:
        arr.append(nums1[i])
        count_1 = count_1 + 1

for i in range(len(nums2)):
    if nums2[i] not in nums1 and nums2[i] not in arr:
        arr.append(nums2[i])
        count_2 = count_2 + 1

result = [arr[:count_1], arr[count_1:]]

print(result)
