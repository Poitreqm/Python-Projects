# 2570. Merge Two 2D Arrays by Summing Values
# You are given two 2D integer arrays nums1 and nums2.
# nums1[i] = [idi, vali] indicate that the number with the id idi has a value equal to vali.
# nums2[i] = [idi, vali] indicate that the number with the id idi has a value equal to vali.
# Each array contains unique ids and is sorted in ascending order by id.
# Merge the two arrays into one array that is sorted in ascending order by id, respecting the following conditions:
# Only ids that appear in at least one of the two arrays should be included in the resulting array.
# Each id should be included only once and its value should be the sum of the values of this id in the two arrays. If the id does not exist in one of the two arrays then its value in that array is considered to be 0.
# Return the resulting array. The returned array must be sorted in ascending order by id.


nums1 = [[1, 2], [2, 3], [4, 5]]
nums2 = [[1, 4], [3, 2], [4, 1]]


arr = nums1 + nums2


d = {}

ans = []

for i in arr:
    key = i[0]
    value = i[1]
    if key in d:
        d[key] += value
    else:
        d[key] = value

for key, value in sorted(d.items()):
    ans.append([key, value])

print(ans)
