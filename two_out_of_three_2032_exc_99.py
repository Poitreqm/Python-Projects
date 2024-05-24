# 2032. Two Out of Three
# Given three integer arrays nums1, nums2, and nums3, return a distinct array containing all the values that are present in at least two out of the three arrays. You may return the values in any order.


nums1 = [1, 1, 3, 2]
nums2 = [2, 3]
nums3 = [3]

n = max(len(nums1), len(nums2), len(nums3))

arr = []

for i in range(len(nums1)):
    if nums1[i] in nums2 or nums1[i] in nums3:
        if nums1[i] not in arr:
            arr.append(nums1[i])
    for j in range(len(nums2)):
        if nums2[j] in nums1 or nums2[j] in nums3:
            if nums2[j] not in arr:
                arr.append(nums2[j])

print(arr)
